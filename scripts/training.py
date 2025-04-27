import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import time
import os
import sys
from collections import deque
import signal

print("TensorFlow version:", tf.__version__)
print(f"Starting high-performance Pong AI training at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# ======================================================================
# Directory and Permission Setup with Verification
# ======================================================================

# Create directories with proper permissions
try:
    # Test main directory
    os.makedirs("models", exist_ok=True)
    test_file = "models/test.txt"
    with open(test_file, "w") as f:
        f.write("Test")
    os.remove(test_file)
    print("✅ Directory permissions verified")
    MODEL_DIR = "models"
except Exception as e:
    print(f"❌ Directory permission error: {str(e)}")
    # Try alternative locations with guaranteed permissions
    MODEL_DIR = '/kaggle/working'
    os.makedirs(MODEL_DIR, exist_ok=True)
    print(f"Using alternative directory: {MODEL_DIR}")

# Set random seeds for reproducibility
np.random.seed(123)
tf.random.set_seed(123)
random.seed(123)

# ======================================================================
# Force Save Helper Function
# ======================================================================

def force_save_model(model, name, counter=0):
    locations = [
        f"{MODEL_DIR}/{name}.keras",
        f"/kaggle/working/{name}.keras",
        f"/tmp/{name}.keras"
    ]
    
    for loc in locations:
        try:
            os.makedirs(os.path.dirname(loc), exist_ok=True)
            model.save(loc)
            if os.path.exists(loc):
                print(f"✅ Model successfully force-saved to {loc}")
                return loc
        except Exception as e:
            print(f"❌ Failed to save to {loc}: {str(e)}")

    try:
        weights_path = f"{MODEL_DIR}/{name}_weights_{counter}.weights.h5"
        model.save_weights(weights_path)
        print(f"✅ Saved weights only to {weights_path}")
        return weights_path
    except Exception as e:
        print(f"❌ Failed to save weights: {str(e)}")

    print("⚠️ ALL SAVE ATTEMPTS FAILED!")
    return None


# ======================================================================
# Interrupt Handler
# ======================================================================

def signal_handler(sig, frame):
    print("\n⚠️ Training interrupted! Attempting to save final model...")
    if 'agent' in globals():
        force_save_model(agent.model, "pong_interrupted_final")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# ======================================================================
# High-Performance Pong Environment
# ======================================================================

class PongEnv:
    """Pong environment optimized for high performance training"""
    def __init__(self, width=400, height=300):
        # Game dimensions
        self.width = width
        self.height = height
        
        # Game elements
        self.paddle_height = 50
        self.paddle_width = 10
        self.ball_radius = 5
        
        # Physics constants
        self.paddle_speed = 15
        self.ball_speed_increase = 1.05
        self.max_ball_speed = 15
        self.initial_ball_speed = 7
        self.spin_factor = 0.6  # Higher spin effect for more realistic bounces
        
        # Game state
        self.rally_length = 0
        self.max_rally_length = 0
        self.score_left = 0
        self.score_right = 0
        
        # Reset to initialize
        self.reset()
    
    def reset(self):
        # Reset paddles
        self.left_paddle_y = self.height / 2 - self.paddle_height / 2
        self.right_paddle_y = self.height / 2 - self.paddle_height / 2
        
        # Reset ball to center
        self.ball_x = self.width / 2
        self.ball_y = self.height / 2
        
        # Initial velocity (randomized direction)
        angle = np.random.uniform(-np.pi/3, np.pi/3)  # Wider angle range
        
        # 70% chance to start toward the agent for better learning
        if np.random.random() < 0.7:
            self.ball_vel_x = self.initial_ball_speed * np.cos(angle)
        else:
            self.ball_vel_x = -self.initial_ball_speed * np.cos(angle)
            
        self.ball_vel_y = self.initial_ball_speed * np.sin(angle)
        
        # Reset rally
        self.rally_length = 0
        
        # Get normalized state
        return self._get_normalized_obs()
    
    def _get_normalized_obs(self):
        """Return normalized observation vector"""
        return np.array([
            self.ball_x / self.width,
            self.ball_y / self.height,
            self.ball_vel_x / self.max_ball_speed,
            self.ball_vel_y / self.max_ball_speed,
            self.left_paddle_y / (self.height - self.paddle_height),
            self.right_paddle_y / (self.height - self.paddle_height),
        ], dtype=np.float32)
    
    def step(self, action):
        """Take one step in the environment"""
        prev_ball_x = self.ball_x  # Remember previous position
        last_right_paddle_y = self.right_paddle_y  # Remember last paddle position
        
        # Process right paddle movement (agent)
        if action == 1:  # Move up
            self.right_paddle_y = max(0, self.right_paddle_y - self.paddle_speed)
        elif action == 2:  # Move down
            self.right_paddle_y = min(self.height - self.paddle_height, 
                                     self.right_paddle_y + self.paddle_speed)
        
        # Process left paddle with advanced AI
        self._update_ai_paddle()
        
        # Move the ball
        self.ball_x += self.ball_vel_x
        self.ball_y += self.ball_vel_y
        
        reward = 0
        done = False
        hit = False
        miss = False
        
        # Wall collisions
        if self.ball_y <= 0 or self.ball_y >= self.height:
            self.ball_vel_y = -self.ball_vel_y
            # Keep ball in bounds
            self.ball_y = np.clip(self.ball_y, 0, self.height)
        
        # Left paddle collision (AI)
        if (self.ball_x <= self.paddle_width and 
            self.ball_y >= self.left_paddle_y and 
            self.ball_y <= self.left_paddle_y + self.paddle_height):
            
            # Advanced collision physics
            rel_intersect_y = (self.ball_y - self.left_paddle_y) / self.paddle_height
            bounce_angle = rel_intersect_y * np.pi/3 - np.pi/6  # -30° to +30°
            
            # Set new velocity based on bounce angle
            speed = min(np.sqrt(self.ball_vel_x**2 + self.ball_vel_y**2) * self.ball_speed_increase, 
                        self.max_ball_speed)
            self.ball_vel_x = speed * np.cos(bounce_angle)
            self.ball_vel_y = speed * np.sin(bounce_angle)
            
            # Ensure ball doesn't get stuck in paddle
            self.ball_x = self.paddle_width + 1
            
            # Increment rally
            self.rally_length += 1
            
            # Small reward for opponent hitting (continuation of rally)
            reward += 0.1
        
        # Right paddle collision (agent)
        if (self.ball_x >= self.width - self.paddle_width and 
            self.ball_y >= self.right_paddle_y and 
            self.ball_y <= self.right_paddle_y + self.paddle_height):
            
            # Advanced collision physics
            rel_intersect_y = (self.ball_y - self.right_paddle_y) / self.paddle_height
            bounce_angle = np.pi - (rel_intersect_y * np.pi/3 - np.pi/6)  # 150° to 210°
            
            # Add spin effect based on paddle movement
            paddle_dy = self.right_paddle_y - last_right_paddle_y
            bounce_angle -= (paddle_dy / self.paddle_speed) * self.spin_factor
            
            # Set new velocity based on bounce angle
            speed = min(np.sqrt(self.ball_vel_x**2 + self.ball_vel_y**2) * self.ball_speed_increase, 
                        self.max_ball_speed)
            self.ball_vel_x = speed * np.cos(bounce_angle)
            self.ball_vel_y = speed * np.sin(bounce_angle)
            
            # Ensure ball doesn't get stuck in paddle
            self.ball_x = self.width - self.paddle_width - 1
            
            # Increment rally
            self.rally_length += 1
            self.max_rally_length = max(self.max_rally_length, self.rally_length)
            
            # Good reward for hitting the ball
            hit = True
            reward += 1.0
            
            # Additional reward for good hits (middle of paddle)
            center_factor = 1.0 - 2 * abs(rel_intersect_y - 0.5)  # 1.0 at center, 0 at edges
            reward += 0.5 * center_factor
        
        # Scoring
        if self.ball_x > self.width:  # AI scores
            self.score_left += 1
            reward -= 1.0  # Negative reward for missing
            miss = True
            done = True  # End episode on score
        
        if self.ball_x < 0:  # Agent scores
            self.score_right += 1
            reward += 2.0  # Higher reward for scoring
            done = True  # End episode on score
            
        # Reward for moving toward ball (position-based reward)
        # Only when ball is moving toward the paddle
        if prev_ball_x < self.ball_x:
            paddle_center = self.right_paddle_y + self.paddle_height / 2
            ball_distance = abs(paddle_center - self.ball_y)
            # Higher reward for better alignment
            alignment_reward = 0.03 * (1.0 - ball_distance / self.height)
            reward += alignment_reward
            
            # Extra reward for moving in correct direction to intercept
            if (action == 1 and self.ball_y < paddle_center) or \
               (action == 2 and self.ball_y > paddle_center):
                reward += 0.05
        
        # Info dictionary with detailed metrics
        info = {
            "hit": hit, 
            "miss": miss,
            "rally_length": self.rally_length,
            "max_rally_length": self.max_rally_length,
            "scores": [self.score_left, self.score_right]
        }
        
        return self._get_normalized_obs(), reward, done, info
    
    def _update_ai_paddle(self):
        """Advanced AI opponent with prediction and difficulty adjustment"""
        # Target y position with prediction
        if self.ball_vel_x < 0:
            # Ball is moving toward AI paddle
            time_to_reach = abs((self.ball_x - self.paddle_width) / self.ball_vel_x)
            predicted_y = self.ball_y + self.ball_vel_y * time_to_reach
            
            # Handle bounces for better prediction
            while predicted_y < 0 or predicted_y > self.height:
                if predicted_y < 0:
                    predicted_y = -predicted_y
                elif predicted_y > self.height:
                    predicted_y = 2 * self.height - predicted_y
            
            # Add some imperfection (20% error)
            error = 0.2 * self.height * np.random.normal(0, 1)
            target_y = predicted_y + error
        else:
            # Ball moving away, return to center
            target_y = self.height / 2
            
        # Determine paddle center target
        paddle_center_target = target_y - self.paddle_height / 2
        paddle_center_target = np.clip(paddle_center_target, 0, self.height - self.paddle_height)
        
        # Move paddle with limited speed
        if self.left_paddle_y < paddle_center_target:
            self.left_paddle_y += min(self.paddle_speed * 0.8, paddle_center_target - self.left_paddle_y)
        else:
            self.left_paddle_y -= min(self.paddle_speed * 0.8, self.left_paddle_y - paddle_center_target)


# ======================================================================
# Replay Buffer for Experience Replay
# ======================================================================

class ReplayBuffer:
    """Experience replay buffer to store and sample transitions"""
    def __init__(self, capacity=50000):
        self.buffer = deque(maxlen=capacity)
        
    def add(self, state, action, reward, next_state, done):
        """Add experience to buffer"""
        self.buffer.append((state, action, reward, next_state, done))
        
    def sample(self, batch_size):
        """Sample a batch of experiences"""
        if len(self.buffer) < batch_size:
            return None
        samples = random.sample(self.buffer, batch_size)
        states, actions, rewards, next_states, dones = map(np.array, zip(*samples))
        return states, actions, rewards, next_states, dones
        
    def __len__(self):
        return len(self.buffer)


# ======================================================================
# DQN Agent with Improved Error Handling and Saving
# ======================================================================

class DQNAgent:
    """DQN Agent with Double Q-learning and proper error handling"""
    def __init__(self, state_dim, action_dim):
        self.state_dim = state_dim
        self.action_dim = action_dim
        
        # Hyperparameters
        self.gamma = 0.99  # Discount factor
        self.epsilon = 1.0  # Starting exploration rate
        self.epsilon_min = 0.05  # Minimum exploration
        self.epsilon_decay = 0.9995  # Slower decay for better exploration
        self.learning_rate = 0.0005  # Learning rate
        self.tau = 0.01  # Soft update rate
        self.batch_size = 64  # Default batch size
        
        # Statistics
        self.loss_history = []
        self.reward_history = []
        self.hits = 0
        self.misses = 0
        self.training_steps = 0
        self.last_10_losses = deque(maxlen=10)
        
        # Experience replay buffer
        self.memory = ReplayBuffer(capacity=50000)
        
        # Build models with error handling
        try:
            print("Building neural network models...")
            self.model = self._build_model()
            self.target_model = self._build_model()
            self.update_target()
            print("Models built successfully!")
        except Exception as e:
            print(f"Error building models: {str(e)}")
            raise
    
    def _build_model(self):
        """Build a DQN model with better error handling"""
        try:
            # Input layer
            inputs = tf.keras.layers.Input(shape=(self.state_dim,))
            
            # Hidden layers
            x = tf.keras.layers.Dense(128, activation='relu')(inputs)
            x = tf.keras.layers.Dense(128, activation='relu')(x)
            
            # Output layer - Q values for each action
            outputs = tf.keras.layers.Dense(self.action_dim, activation='linear')(x)
            
            # Create model
            model = tf.keras.models.Model(inputs=inputs, outputs=outputs)
            
            # Compile with MSE loss (more compatible than huber across TF versions)
            model.compile(
                optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate),
                loss='mse'  # Using MSE instead of huber for compatibility
            )
            
            # Print model summary
            model.summary()
            
            return model
            
        except Exception as e:
            print(f"Failed to build model: {str(e)}")
            raise
    
    def update_target(self):
        """Copy weights from main model to target model"""
        self.target_model.set_weights(self.model.get_weights())
        
    def soft_update_target(self):
        """Soft update target network weights"""
        model_weights = self.model.get_weights()
        target_weights = self.target_model.get_weights()
        
        for i in range(len(model_weights)):
            target_weights[i] = self.tau * model_weights[i] + (1 - self.tau) * target_weights[i]
            
        self.target_model.set_weights(target_weights)
    
    def remember(self, state, action, reward, next_state, done):
        """Store experience in memory"""
        self.memory.add(state, action, reward, next_state, done)
    
    def act(self, state, training=True):
        """Choose action using epsilon-greedy policy"""
        if training and np.random.rand() < self.epsilon:
            return random.randrange(self.action_dim)
        
        try:
            # Reshape state for model input
            state_tensor = np.array([state])  # Add batch dimension
            
            # Predict Q-values
            q_values = self.model.predict(state_tensor, verbose=0)[0]
            
            # Return action with highest Q-value
            return np.argmax(q_values)
            
        except Exception as e:
            print(f"Error during action selection: {str(e)}")
            print(f"State shape: {state.shape}, values: {state}")
            # Return random action as fallback
            return random.randrange(self.action_dim)
    
    def replay(self, batch_size=None):
        """Train the model on a batch of experiences"""
        if batch_size is None:
            batch_size = self.batch_size
            
        # Sample batch from replay buffer
        batch = self.memory.sample(batch_size)
        
        # Not enough samples yet
        if batch is None:
            return None
            
        states, actions, rewards, next_states, dones = batch
        
        try:
            # Double DQN implementation
            
            # 1. Get next actions from main model
            next_q_values = self.model.predict(next_states, verbose=0)
            next_actions = np.argmax(next_q_values, axis=1)
            
            # 2. Get Q values from target model for those actions
            target_q_values = self.target_model.predict(next_states, verbose=0)
            target_q = np.array([target_q_values[i, next_actions[i]] 
                               for i in range(batch_size)])
            
            # 3. Calculate target using Bellman equation
            targets = rewards + self.gamma * target_q * (1 - dones)
            
            # 4. Predict current Q values
            current_q = self.model.predict(states, verbose=0)
            
            # 5. Update targets for actions taken
            for i, action in enumerate(actions):
                current_q[i, action] = targets[i]
            
            # 6. Train model
            history = self.model.fit(
                states, current_q, 
                verbose=0,
                batch_size=batch_size
            )
            
            # Store loss
            loss = history.history['loss'][0]
            self.loss_history.append(loss)
            self.last_10_losses.append(loss)
            
            # Increment training steps
            self.training_steps += 1
            
            return loss
            
        except Exception as e:
            print(f"\nError during replay: {str(e)}")
            print(f"Batch shapes - states: {states.shape}, actions: {actions.shape}, rewards: {rewards.shape}")
            return None
    
    def update_epsilon(self):
        """Decay exploration rate"""
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
    
    def save(self, filepath):
        """Save model with improved error handling and diagnostics"""
        try:
            # Make sure the directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Get the full path
            full_path = os.path.abspath(filepath)
            print(f"Attempting to save model to: {full_path}")
            
            # Save the model
            self.model.save(filepath)
            
            # Verify the save worked
            if os.path.exists(filepath):
                size_kb = os.path.getsize(filepath) / 1024
                print(f"✅ Model successfully saved to {filepath} ({size_kb:.1f} KB)")
                return True
            else:
                print(f"❌ Model file not created: {filepath}")
                return False
        except Exception as e:
            print(f"❌ Error saving model: {str(e)}")
            import traceback
            traceback.print_exc()
            
            # Try alternative location
            try:
                alt_path = os.path.join(MODEL_DIR, os.path.basename(filepath))
                print(f"Trying alternative location: {alt_path}")
                self.model.save(alt_path)
                print(f"✅ Model saved to alternative location: {alt_path}")
                return True
            except Exception as e2:
                print(f"❌ Alternative save also failed: {str(e2)}")
                return False
            
    def get_stats(self):
        """Get agent statistics"""
        return {
            'epsilon': self.epsilon,
            'memory_size': len(self.memory.buffer),
            'training_steps': self.training_steps,
            'avg_loss': np.mean(self.last_10_losses) if self.last_10_losses else 0,
            'hits': self.hits,
            'misses': self.misses
        }


# ======================================================================
# TFLite Converter with Error Handling
# ======================================================================

def convert_to_tflite(model_path, output_path):
    """Convert model to TFLite format with error handling"""
    print(f"\nConverting model at {model_path} to TFLite format...")
    
    try:
        # Load the Keras model
        model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully")
        
        # Create converter
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        
        # Set optimization level
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
        
        # Convert model
        print("Converting model to TFLite (this may take a moment)...")
        tflite_model = converter.convert()
        
        # Try multiple save locations
        save_locations = [output_path, f"{MODEL_DIR}/{os.path.basename(output_path)}", "/kaggle/working/pong_ai_model.tflite"]
        success = False
        
        for save_path in save_locations:
            try:
                # Ensure directory exists
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                
                # Save model to file
                with open(save_path, 'wb') as f:
                    f.write(tflite_model)
                
                model_size = len(tflite_model) / 1024.0
                print(f"✅ TFLite model saved to {save_path}")
                print(f"✅ Model size: {model_size:.1f} KB")
                success = True
                break
            except Exception as e:
                print(f"❌ Failed to save TFLite model to {save_path}: {str(e)}")
        
        return success, len(tflite_model) / 1024.0
        
    except Exception as e:
        print(f"❌ Error converting model to TFLite: {str(e)}")
        return False, 0


# ======================================================================
# High-Quality Training Loop with Robust Error Handling
# ======================================================================

def evaluate_agent(agent, env, episodes=20):
    """Evaluate agent without exploration"""
    print(f"\nEvaluating agent performance over {episodes} episodes...")
    
    hits = 0
    misses = 0
    
    for ep in range(1, episodes+1):
        state = env.reset()
        done = False
        steps = 0
        max_steps = 500
        
        while not done and steps < max_steps:
            action = agent.act(state, training=False)  # No exploration
            next_state, _, done, info = env.step(action)
            state = next_state
            steps += 1
            
            # Track hits and misses
            if info.get("hit", False):
                hits += 1
            if info.get("miss", False):
                misses += 1
        
        # Print progress
        if ep % 5 == 0 or ep == episodes:
            print(f"  Evaluation progress: {ep}/{episodes} episodes")
            sys.stdout.flush()
    
    # Calculate hit rate
    hit_rate = hits / (hits + misses) if (hits + misses) > 0 else 0
    print(f"  Evaluation hit rate: {hit_rate:.3f} ({hits} hits, {misses} misses)")
    
    return hit_rate

def train_high_quality_model(episodes=1000, target_hit_rate=0.9, save_freq=50):
    """Train model with detailed progress updates and error handling"""
    print("\n" + "="*80)
    print(" HIGH-PERFORMANCE PONG AI TRAINING ".center(80, "="))
    print("="*80)
    print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Target hit rate: {target_hit_rate*100:.1f}%")
    print(f"Maximum episodes: {episodes}")
    print(f"Model directory: {MODEL_DIR}")
    print("="*80)
    
    # Force output
    sys.stdout.flush()
    
    try:
        # Create environment and agent
        print("Initializing environment and agent...")
        env = PongEnv()
        agent = DQNAgent(state_dim=6, action_dim=3)
        print("Initialization complete!")
        
        # Training variables
        scores = []
        best_hit_rate = 0
        best_avg_score = -float('inf')
        hit_streak = 0  # Track consecutive hits
        
        # Time tracking
        start_time = time.time()
        last_update = start_time
        update_interval = 10  # Update every 10 seconds for more feedback
        
        # Adding time-based save interval
        last_save_time = start_time
        save_interval = 5 * 60  # Save every 5 minutes regardless of episodes
        
        # Print header for progress table
        print("\n" + "-"*120)
        print("| Time     | Ep   | Score | Avg Score | Epsilon  | Hit Rate | Streak | Rally | Steps | Loss    | Memory  |")
        print("-"*120)
        
        # Main training loop
        for episode in range(1, episodes+1):
            episode_start = time.time()
            
            # Reset environment
            state = env.reset()
            episode_reward = 0
            episode_steps = 0
            episode_hits = 0
            episode_misses = 0
            max_steps = 500  # Prevent infinite episodes
            done = False
            
            # Episode loop
            while not done and episode_steps < max_steps:
                # Select and take action
                action = agent.act(state)
                next_state, reward, done, info = env.step(action)
                
                # Store experience
                agent.remember(state, action, reward, next_state, done)
                
                # Track hits and misses
                if info.get("hit", False):
                    episode_hits += 1
                    agent.hits += 1
                    hit_streak += 1
                if info.get("miss", False):
                    episode_misses += 1
                    agent.misses += 1
                    hit_streak = 0
                
                # Update state and reward
                state = next_state
                episode_reward += reward
                episode_steps += 1
            
            # Train agent (multiple times for better learning)
            losses = []
            for _ in range(4):  # Train 4 times per episode
                loss = agent.replay(batch_size=64)
                if loss is not None:
                    losses.append(loss)
            
            # Compute average loss for this episode
            avg_loss = np.mean(losses) if losses else 0
            
            # Decay exploration rate
            agent.update_epsilon()
            
            # Soft update target network
            agent.soft_update_target()
            
            # Hard update target network periodically
            if episode % 100 == 0:
                agent.update_target()
            
            # Store score
            scores.append(episode_reward)
            avg_score = np.mean(scores[-100:]) if len(scores) >= 100 else np.mean(scores)
            
            # Calculate hit rate
            hit_rate = agent.hits / (agent.hits + agent.misses) if (agent.hits + agent.misses) > 0 else 0
            
            # Get current time
            current_time = time.time()
            
            # Display progress every 10 seconds or on first/last episode
            time_elapsed = current_time - last_update
            if time_elapsed >= update_interval or episode == 1 or episode == episodes:
                # Format time
                time_str = time.strftime('%H:%M:%S')
                
                # Get memory usage
                memory_size = len(agent.memory.buffer)
                
                # Get max rally length
                max_rally = getattr(env, 'max_rally_length', 0)
                
                # Print progress row
                print(f"| {time_str} | {episode:4d} | {episode_reward:5.1f} | {avg_score:9.1f} | {agent.epsilon:.7f} | {hit_rate:.3f} | {hit_streak:6d} | {max_rally:5d} | {agent.training_steps:5d} | {avg_loss:.6f} | {memory_size:7d} |")
                sys.stdout.flush()
                
                # Update last update time
                last_update = current_time
            
            # Check time-based save interval
            save_time_elapsed = current_time - last_save_time
            if save_time_elapsed >= save_interval:
                save_path = force_save_model(agent.model, f"pong_time_{int(current_time)}", episode)
                print(f"⏱️ Time-based checkpoint saved at {save_path}")
                last_save_time = current_time
                sys.stdout.flush()
            
            # Save model at episode intervals
            if episode % save_freq == 0:
                save_path = os.path.join(MODEL_DIR, f"pong_ep{episode}.keras")
                agent.save(save_path)
                print(f"📊 Episode checkpoint saved at episode {episode}")
                sys.stdout.flush()
            
            # Save best model based on hit rate
            if hit_rate > best_hit_rate and episode > 50 and agent.hits > 100:
                best_hit_rate = hit_rate
                force_save_model(agent.model, "pong_best_hitrate")
                print(f"\n⭐ New best hit rate: {best_hit_rate:.3f} saved!")
                sys.stdout.flush()
            
            # Save best model based on score
            if avg_score > best_avg_score and episode > 50:
                best_avg_score = avg_score
                force_save_model(agent.model, "pong_best_score")
            
            # Every 200 episodes, force save regardless
            if episode % 200 == 0:
                force_save_model(agent.model, f"pong_milestone_{episode}")
                print(f"🏆 Milestone save at episode {episode}")
            
            # Check if we've reached target hit rate
            if episode > 200 and hit_rate >= target_hit_rate and agent.hits > 500:
                # Optional: Evaluate to confirm hit rate is stable
                eval_hr = evaluate_agent(agent, env, episodes=20)
                if eval_hr >= target_hit_rate:
                    print(f"\n🎯 Target hit rate achieved: {eval_hr:.3f}")
                    force_save_model(agent.model, "pong_target_achieved")
                    break
        
        # Training complete
        training_time = (time.time() - start_time) / 60.0
        
        print("\n" + "="*80)
        print(f"Training complete after {episode} episodes!")
        print(f"Total time: {training_time:.1f} minutes")
        print(f"Final hit rate: {hit_rate:.3f}")
        print(f"Best hit rate achieved: {best_hit_rate:.3f}")
        print(f"Total hits: {agent.hits}, Total misses: {agent.misses}")
        print("="*80)
        
        # Save final model (try multiple locations)
        force_save_model(agent.model, "pong_final")
        
        # Convert best model to TFLite
        best_model_path = os.path.join(MODEL_DIR, "pong_best_hitrate")
        fallback_path = os.path.join(MODEL_DIR, "pong_final")
        
        if os.path.exists(best_model_path):
            success, model_size = convert_to_tflite(best_model_path, "pong_ai_model.tflite")
        elif os.path.exists(fallback_path):
            success, model_size = convert_to_tflite(fallback_path, "pong_ai_model.tflite")
        else:
            # Find any model file we can use
            for path in [MODEL_DIR, "/kaggle/working", "/tmp"]:
                try:
                    model_files = [f for f in os.listdir(path) if "pong_" in f and os.path.isdir(os.path.join(path, f))]
                    if model_files:
                        model_path = os.path.join(path, model_files[0])
                        print(f"Using found model: {model_path}")
                        success, model_size = convert_to_tflite(model_path, "pong_ai_model.tflite")
                        break
                except Exception as e:
                    print(f"Error checking path {path}: {e}")
        
        return hit_rate, scores
        
    except Exception as e:
        print(f"\n❌ Error during training: {str(e)}")
        import traceback
        traceback.print_exc()
        
        # Try to save whatever we have
        if 'agent' in locals():
            force_save_model(agent.model, "pong_emergency_save")
        
        return 0.0, []


# ======================================================================
# Run Training
# ======================================================================

try:
    print("\nStarting training process...")
    # Start with more episodes to ensure we reach target hit rate
    hit_rate, scores = train_high_quality_model(
        episodes=2000,        # Up to 2000 episodes
        target_hit_rate=0.9,  # 90% hit rate target
        save_freq=50          # Save every 50 episodes
    )
    
    # Plot results if training completed
    if len(scores) > 0:
        plt.figure(figsize=(10, 6))
        plt.plot(scores)
        plt.title('Training Progress')
        plt.xlabel('Episode')
        plt.ylabel('Score')
        plt.grid(True, alpha=0.3)
        plt.savefig('training_results.png')
        
    print("\nTraining process complete!")
    print(f"Final hit rate: {hit_rate:.3f}")
    print("Your TFLite model is ready for use in your Flutter app!")
    
except Exception as e:
    print(f"\n❌ Critical error: {str(e)}")
    import traceback
    traceback.print_exc()


# ======================================================================
# Final Status Check
# ======================================================================

print("\n=== FINAL STATUS CHECK ===")

# Check for model files
for path in [MODEL_DIR, "/kaggle/working", "/tmp"]:
    try:
        files = os.listdir(path)
        model_files = [f for f in files if "pong" in f]
        print(f"Files in {path}: {model_files}")
    except Exception as e:
        print(f"Cannot list {path}: {str(e)}")

# Check for TFLite model
tflite_paths = ["pong_ai_model.tflite", 
               f"{MODEL_DIR}/pong_ai_model.tflite", 
               "/kaggle/working/pong_ai_model.tflite"]

for tflite_path in tflite_paths:
    if os.path.exists(tflite_path):
        size_kb = os.path.getsize(tflite_path) / 1024
        print(f"✅ Final TFLite model found: {tflite_path} ({size_kb:.1f} KB)")
        break
else:
    print("❌ TFLite model not found in any location!")

print("\nTraining Complete! Don't forget to download your pong_ai_model.tflite file.")
