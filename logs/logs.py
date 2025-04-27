TensorFlow version: 2.18.0
Starting high-performance Pong AI training at 2025-04-26 00:50:46
✅ Directory permissions verified

Starting training process...

================================================================================
====================== HIGH-PERFORMANCE PONG AI TRAINING =======================
================================================================================
Start time: 2025-04-26 00:50:46
Target hit rate: 90.0%
Maximum episodes: 2000
Model directory: models
================================================================================
Initializing environment and agent...
Building neural network models...
Model: "functional_2"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ input_layer_2 (InputLayer)           │ (None, 6)                   │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_6 (Dense)                      │ (None, 128)                 │             896 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_7 (Dense)                      │ (None, 128)                 │          16,512 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_8 (Dense)                      │ (None, 3)                   │             387 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
 Total params: 17,795 (69.51 KB)
 Trainable params: 17,795 (69.51 KB)
 Non-trainable params: 0 (0.00 B)
Model: "functional_3"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ input_layer_3 (InputLayer)           │ (None, 6)                   │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_9 (Dense)                      │ (None, 128)                 │             896 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_10 (Dense)                     │ (None, 128)                 │          16,512 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_11 (Dense)                     │ (None, 3)                   │             387 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
 Total params: 17,795 (69.51 KB)
 Trainable params: 17,795 (69.51 KB)
 Non-trainable params: 0 (0.00 B)
Models built successfully!
Initialization complete!

------------------------------------------------------------------------------------------------------------------------
| Time     | Ep   | Score | Avg Score | Epsilon  | Hit Rate | Streak | Rally | Steps | Loss    | Memory  |
------------------------------------------------------------------------------------------------------------------------
| 00:50:46 |    1 |   0.3 |       0.3 | 0.9995000 | 0.000 |      0 |     0 |     0 | 0.000000 |      34 |
| 00:50:56 |   11 |   1.3 |       2.4 | 0.9945137 | 0.375 |      0 |     4 |    40 | 0.012451 |    1206 |
| 00:51:06 |   23 |   0.4 |       1.7 | 0.9885630 | 0.259 |      0 |     4 |    88 | 0.002251 |    1923 |
| 00:51:16 |   34 |   3.1 |       1.7 | 0.9831395 | 0.256 |      0 |     4 |   132 | 0.008363 |    2690 |
| 00:51:27 |   45 |   1.4 |       1.8 | 0.9777457 | 0.273 |      0 |     4 |   176 | 0.001866 |    3919 |
Attempting to save model to: /kaggle/working/models/pong_ep50.keras
✅ Model successfully saved to models/pong_ep50.keras (231.1 KB)
📊 Episode checkpoint saved at episode 50
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:51:37 |   55 |   0.6 |       1.8 | 0.9728680 | 0.275 |      0 |     4 |   216 | 0.007412 |    5084 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:51:48 |   66 |   0.9 |       1.7 | 0.9675306 | 0.272 |      0 |     4 |   260 | 0.001827 |    5886 |
| 00:51:58 |   76 |   0.5 |       1.7 | 0.9627038 | 0.269 |      0 |     4 |   300 | 0.004621 |    6780 |
| 00:52:09 |   88 |   0.4 |       1.5 | 0.9569434 | 0.238 |      0 |     4 |   348 | 0.005588 |    7263 |
| 00:52:19 |   98 |   7.8 |       1.6 | 0.9521695 | 0.244 |      0 |     4 |   388 | 0.010259 |    8290 |
Attempting to save model to: /kaggle/working/models/pong_ep100.keras
✅ Model successfully saved to models/pong_ep100.keras (231.1 KB)
📊 Episode checkpoint saved at episode 100
| 00:52:30 |  108 |   0.4 |       1.5 | 0.9474193 | 0.237 |      0 |     4 |   428 | 0.009062 |    8950 |
| 00:52:41 |  116 |   0.1 |       1.6 | 0.9436363 | 0.246 |      0 |     4 |   460 | 0.009410 |    9827 |
| 00:52:51 |  125 |   0.5 |       1.6 | 0.9393984 | 0.247 |      0 |     4 |   496 | 0.001776 |   10542 |
| 00:53:02 |  134 |   3.3 |       1.6 | 0.9351795 | 0.247 |      0 |     4 |   532 | 0.009759 |   11363 |
| 00:53:13 |  143 |   0.7 |       1.6 | 0.9309796 | 0.249 |      0 |     4 |   568 | 0.006817 |   12250 |
Attempting to save model to: /kaggle/working/models/pong_ep150.keras
✅ Model successfully saved to models/pong_ep150.keras (231.1 KB)
📊 Episode checkpoint saved at episode 150
| 00:53:23 |  151 |   3.5 |       1.6 | 0.9272622 | 0.254 |      0 |     4 |   600 | 0.006133 |   13085 |
| 00:53:34 |  161 |   1.5 |       1.6 | 0.9226363 | 0.252 |      0 |     4 |   640 | 0.006915 |   13969 |
| 00:53:45 |  171 |   3.9 |       1.7 | 0.9180335 | 0.255 |      0 |     4 |   680 | 0.007906 |   14885 |
| 00:53:56 |  179 |   1.6 |       1.7 | 0.9143678 | 0.259 |      0 |     4 |   712 | 0.001798 |   15847 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:54:06 |  187 |   0.7 |       1.9 | 0.9107167 | 0.267 |      0 |     4 |   744 | 0.010332 |   16645 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:54:17 |  195 |   0.1 |       2.0 | 0.9070802 | 0.268 |      0 |     4 |   776 | 0.008651 |   17397 |
Attempting to save model to: /kaggle/working/models/pong_ep200.keras
✅ Model successfully saved to models/pong_ep200.keras (231.1 KB)
📊 Episode checkpoint saved at episode 200
✅ Model successfully force-saved to models/pong_milestone_200.keras
🏆 Milestone save at episode 200
| 00:54:28 |  203 |   0.3 |       2.0 | 0.9034582 | 0.268 |      0 |     5 |   808 | 0.006628 |   18117 |
| 00:54:39 |  212 |   3.2 |       1.9 | 0.8994008 | 0.268 |      0 |     5 |   844 | 0.002023 |   18847 |
| 00:54:50 |  220 |   0.2 |       2.0 | 0.8958095 | 0.268 |      0 |     5 |   876 | 0.002874 |   19412 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:55:00 |  227 |   0.3 |       2.0 | 0.8926789 | 0.271 |      0 |     5 |   904 | 0.001973 |   20276 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:55:10 |  235 |   0.2 |       2.0 | 0.8891144 | 0.269 |      0 |     5 |   936 | 0.008079 |   20822 |
| 00:55:21 |  242 |   0.2 |       1.9 | 0.8860071 | 0.270 |      0 |     5 |   964 | 0.005002 |   21513 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:55:31 |  249 |   2.8 |       2.1 | 0.8829108 | 0.280 |      0 |     6 |   992 | 0.008194 |   22373 |
Attempting to save model to: /kaggle/working/models/pong_ep250.keras
✅ Model successfully saved to models/pong_ep250.keras (231.1 KB)
📊 Episode checkpoint saved at episode 250
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:55:42 |  256 |   1.2 |       2.1 | 0.8798252 | 0.283 |      0 |     6 |  1020 | 0.005144 |   23030 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_time_1745628947.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745628947.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:55:52 |  261 |   0.5 |       2.2 | 0.8776279 | 0.287 |      0 |     6 |  1040 | 0.005336 |   23750 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:56:03 |  268 |   4.3 |       2.2 | 0.8745608 | 0.288 |      0 |     6 |  1068 | 0.008550 |   24364 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.288 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.292 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.293 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:56:14 |  275 |   6.1 |       2.3 | 0.8715044 | 0.292 |      1 |     6 |  1096 | 0.008198 |   24997 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.295 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:56:25 |  281 |   0.2 |       2.3 | 0.8688931 | 0.293 |      0 |     6 |  1120 | 0.003792 |   25696 |
| 00:56:35 |  288 |   7.9 |       2.3 | 0.8658566 | 0.296 |      2 |     6 |  1148 | 0.005280 |   26457 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.296 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.298 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.299 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.299 saved!
| 00:56:46 |  295 |   1.0 |       2.3 | 0.8628306 | 0.297 |      0 |     6 |  1176 | 0.011724 |   27191 |
Attempting to save model to: /kaggle/working/models/pong_ep300.keras
✅ Model successfully saved to models/pong_ep300.keras (231.1 KB)
📊 Episode checkpoint saved at episode 300
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:56:59 |  302 |  11.1 |       2.4 | 0.8598152 | 0.302 |      0 |     6 |  1204 | 0.008813 |   28100 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.302 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.308 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.309 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:57:10 |  307 |   3.2 |       2.6 | 0.8576678 | 0.309 |      0 |     7 |  1224 | 0.003925 |   28995 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:57:21 |  315 |   4.0 |       2.5 | 0.8542432 | 0.307 |      1 |     7 |  1256 | 0.003469 |   29509 |
| 00:57:34 |  323 |   4.8 |       2.5 | 0.8508322 | 0.305 |      0 |     7 |  1288 | 0.008666 |   30227 |
| 00:57:45 |  331 |   3.9 |       2.5 | 0.8474348 | 0.303 |      0 |     7 |  1320 | 0.007199 |   30850 |
| 00:57:56 |  338 |   1.5 |       2.5 | 0.8444732 | 0.299 |      0 |     7 |  1348 | 0.009549 |   31260 |
| 00:58:06 |  343 |   2.0 |       2.5 | 0.8423641 | 0.301 |      0 |     7 |  1368 | 0.007858 |   31893 |
| 00:58:17 |  349 |   9.8 |       2.4 | 0.8398402 | 0.301 |      0 |     7 |  1392 | 0.010097 |   32583 |
Attempting to save model to: /kaggle/working/models/pong_ep350.keras
✅ Model successfully saved to models/pong_ep350.keras (231.1 KB)
📊 Episode checkpoint saved at episode 350
| 00:58:28 |  354 |   7.8 |       2.5 | 0.8377427 | 0.304 |      0 |     7 |  1412 | 0.003793 |   33235 |
| 00:58:38 |  360 |   0.5 |       2.4 | 0.8352326 | 0.303 |      0 |     7 |  1436 | 0.004010 |   33777 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.311 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 00:58:49 |  365 |   1.4 |       2.6 | 0.8331466 | 0.310 |      0 |     9 |  1456 | 0.008401 |   34633 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.311 saved!
| 00:59:01 |  371 |   2.0 |       2.5 | 0.8306503 | 0.311 |      0 |     9 |  1480 | 0.007578 |   35225 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.312 saved!
| 00:59:11 |  377 |   1.2 |       2.5 | 0.8281615 | 0.309 |      0 |     9 |  1504 | 0.008573 |   35787 |
| 00:59:22 |  383 |   0.1 |       2.5 | 0.8256801 | 0.308 |      0 |     9 |  1528 | 0.007346 |   36291 |
| 00:59:33 |  389 |   7.1 |       2.4 | 0.8232061 | 0.307 |      0 |     9 |  1552 | 0.011354 |   36805 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.312 saved!
| 00:59:43 |  392 |   4.9 |       2.5 | 0.8219719 | 0.313 |      0 |     9 |  1564 | 0.004173 |   37479 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.313 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.315 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.316 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.316 saved!
| 00:59:53 |  396 |   0.5 |       2.6 | 0.8203292 | 0.316 |      0 |     9 |  1580 | 0.007435 |   38135 |
Attempting to save model to: /kaggle/working/models/pong_ep400.keras
✅ Model successfully saved to models/pong_ep400.keras (231.1 KB)
📊 Episode checkpoint saved at episode 400
✅ Model successfully force-saved to models/pong_milestone_400.keras
🏆 Milestone save at episode 400
| 01:00:06 |  402 |  11.5 |       2.6 | 0.8178713 | 0.317 |      0 |     9 |  1604 | 0.008211 |   38906 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.317 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.318 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.319 saved!
| 01:00:18 |  407 |   5.5 |       2.5 | 0.8158287 | 0.319 |      1 |     9 |  1624 | 0.007245 |   39622 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.319 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.319 saved!
| 01:00:28 |  414 |   0.1 |       2.5 | 0.8129776 | 0.316 |      0 |     9 |  1652 | 0.005484 |   40031 |
| 01:00:40 |  419 |   8.6 |       2.5 | 0.8109472 | 0.317 |      0 |     9 |  1672 | 0.002244 |   40729 |
✅ Model successfully force-saved to models/pong_time_1745629247.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745629247.keras
| 01:00:52 |  425 |   5.8 |       2.6 | 0.8085173 | 0.318 |      1 |     9 |  1696 | 0.004700 |   41370 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.320 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:01:03 |  429 |   8.0 |       2.7 | 0.8069015 | 0.321 |      0 |     9 |  1712 | 0.009275 |   42102 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.321 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.322 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.322 saved!
| 01:01:13 |  432 |   5.1 |       2.8 | 0.8056918 | 0.323 |      0 |     9 |  1724 | 0.008378 |   42626 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.323 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:01:26 |  439 |  10.3 |       2.8 | 0.8028761 | 0.323 |      0 |     9 |  1752 | 0.004751 |   43307 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.323 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:01:38 |  445 |   1.4 |       2.8 | 0.8004705 | 0.322 |      0 |     9 |  1776 | 0.007014 |   43802 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.324 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:01:50 |  450 |   3.9 |       2.8 | 0.7984713 | 0.325 |      0 |     9 |  1796 | 0.007463 |   44458 |
Attempting to save model to: /kaggle/working/models/pong_ep450.keras
✅ Model successfully saved to models/pong_ep450.keras (231.1 KB)
📊 Episode checkpoint saved at episode 450
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.325 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.325 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.327 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:02:00 |  454 |   0.6 |       2.9 | 0.7968755 | 0.327 |      0 |     9 |  1812 | 0.011320 |   45049 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.329 saved!
| 01:02:15 |  459 |   8.0 |       3.0 | 0.7948853 | 0.330 |      0 |     9 |  1832 | 0.007205 |   45907 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.330 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:02:25 |  466 |   0.7 |       2.8 | 0.7921074 | 0.328 |      0 |     9 |  1860 | 0.012436 |   46297 |
| 01:02:36 |  472 |   0.5 |       2.7 | 0.7897341 | 0.327 |      0 |     9 |  1884 | 0.004922 |   46734 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.330 saved!
| 01:02:48 |  476 |   4.4 |       2.9 | 0.7881558 | 0.330 |      0 |     9 |  1900 | 0.008569 |   47514 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.330 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.330 saved!
| 01:03:02 |  482 |  12.1 |       3.0 | 0.7857943 | 0.332 |      3 |     9 |  1924 | 0.006802 |   48215 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.332 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:03:12 |  488 |   5.7 |       3.0 | 0.7834398 | 0.330 |      1 |     9 |  1948 | 0.003657 |   48587 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:03:24 |  493 |   4.1 |       2.9 | 0.7814832 | 0.331 |      0 |     9 |  1968 | 0.003614 |   49202 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.332 saved!
| 01:03:36 |  499 |   1.5 |       2.9 | 0.7791417 | 0.331 |      0 |     9 |  1992 | 0.007780 |   49724 |
Attempting to save model to: /kaggle/working/models/pong_ep500.keras
✅ Model successfully saved to models/pong_ep500.keras (231.1 KB)
📊 Episode checkpoint saved at episode 500
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.332 saved!
| 01:03:47 |  505 |   0.4 |       2.7 | 0.7768072 | 0.331 |      0 |     9 |  2016 | 0.001983 |   50000 |
| 01:03:59 |  510 |   7.1 |       2.8 | 0.7748671 | 0.332 |      0 |     9 |  2036 | 0.001440 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.332 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.333 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.334 saved!
| 01:04:10 |  514 |   3.4 |       2.9 | 0.7733185 | 0.334 |      0 |     9 |  2052 | 0.003530 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.334 saved!
| 01:04:21 |  519 |   8.1 |       2.9 | 0.7713871 | 0.334 |      2 |     9 |  2072 | 0.009728 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.335 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.336 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.337 saved!
| 01:04:32 |  523 |   4.3 |       3.0 | 0.7698455 | 0.337 |      0 |     9 |  2088 | 0.006236 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.337 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.338 saved!
| 01:04:43 |  527 |   1.6 |       3.0 | 0.7683070 | 0.338 |      0 |     9 |  2104 | 0.012712 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.340 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:04:54 |  531 |   0.3 |       2.9 | 0.7667715 | 0.339 |      0 |     9 |  2120 | 0.004698 |   50000 |
| 01:05:05 |  536 |   3.8 |       3.0 | 0.7648565 | 0.339 |      0 |     9 |  2140 | 0.008907 |   50000 |
| 01:05:15 |  539 |  14.9 |       3.0 | 0.7637098 | 0.341 |      0 |     9 |  2152 | 0.011580 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.341 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.345 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:05:27 |  543 |   1.1 |       3.1 | 0.7621835 | 0.343 |      0 |     9 |  2168 | 0.008763 |   50000 |
| 01:05:37 |  548 |   1.4 |       3.2 | 0.7602800 | 0.344 |      0 |     9 |  2188 | 0.008074 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep550.keras
✅ Model successfully saved to models/pong_ep550.keras (231.1 KB)
📊 Episode checkpoint saved at episode 550
| 01:05:49 |  553 |   7.0 |       3.0 | 0.7583812 | 0.345 |      0 |     9 |  2208 | 0.006576 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745629549.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745629549.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.345 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.346 saved!
| 01:06:00 |  556 |   7.3 |       3.2 | 0.7572442 | 0.347 |      0 |     9 |  2220 | 0.007160 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.347 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.348 saved!
| 01:06:11 |  559 |   8.2 |       3.2 | 0.7561089 | 0.349 |      0 |     9 |  2232 | 0.004575 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.349 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.351 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:06:23 |  563 |   4.0 |       3.3 | 0.7545978 | 0.351 |      0 |     9 |  2248 | 0.006243 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:06:34 |  568 |   5.1 |       3.3 | 0.7527132 | 0.349 |      0 |     9 |  2268 | 0.007866 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.352 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:06:45 |  571 |   1.3 |       3.4 | 0.7515847 | 0.352 |      0 |     9 |  2280 | 0.003593 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:06:56 |  576 |   4.9 |       3.3 | 0.7497076 | 0.351 |      0 |     9 |  2300 | 0.006668 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.353 saved!
| 01:07:07 |  579 |   0.0 |       3.4 | 0.7485836 | 0.352 |      0 |     9 |  2312 | 0.003568 |   50000 |
| 01:07:20 |  583 |  12.3 |       3.4 | 0.7470875 | 0.355 |      3 |     9 |  2328 | 0.012437 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.355 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.358 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:07:31 |  586 |   3.7 |       3.6 | 0.7459675 | 0.358 |      0 |     9 |  2340 | 0.008808 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:07:42 |  589 |   7.8 |       3.6 | 0.7448491 | 0.359 |      0 |     9 |  2352 | 0.003096 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.359 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.359 saved!
| 01:07:55 |  593 |   7.2 |       3.7 | 0.7433605 | 0.360 |      0 |     9 |  2368 | 0.011886 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.360 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.362 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:08:07 |  595 |  12.0 |       3.8 | 0.7426173 | 0.364 |      0 |     9 |  2376 | 0.001822 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.364 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:08:20 |  599 |  11.1 |       3.9 | 0.7411332 | 0.365 |      0 |     9 |  2392 | 0.004640 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.365 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
Attempting to save model to: /kaggle/working/models/pong_ep600.keras
✅ Model successfully saved to models/pong_ep600.keras (231.1 KB)
📊 Episode checkpoint saved at episode 600
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.365 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_milestone_600.keras
🏆 Milestone save at episode 600
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.366 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:08:30 |  603 |   0.9 |       3.9 | 0.7396521 | 0.365 |      0 |     9 |  2408 | 0.000586 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.367 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.367 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:08:43 |  607 |   8.3 |       4.1 | 0.7381739 | 0.369 |      2 |     9 |  2424 | 0.004257 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.369 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.369 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.370 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:08:54 |  610 |   1.4 |       4.1 | 0.7370672 | 0.370 |      0 |     9 |  2436 | 0.002831 |   50000 |
| 01:09:06 |  613 |  10.7 |       4.2 | 0.7359621 | 0.372 |      0 |     9 |  2448 | 0.004416 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.372 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.373 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:09:22 |  617 |  13.0 |       4.4 | 0.7344913 | 0.375 |      5 |     9 |  2464 | 0.001037 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.375 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.377 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:09:32 |  620 |   0.1 |       4.4 | 0.7333901 | 0.377 |      0 |     9 |  2476 | 0.003158 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.378 saved!
| 01:09:42 |  623 |   0.2 |       4.4 | 0.7322906 | 0.377 |      0 |     9 |  2488 | 0.004124 |   50000 |
| 01:09:54 |  629 |   0.6 |       4.2 | 0.7300964 | 0.377 |      0 |     9 |  2512 | 0.000607 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.378 saved!
| 01:10:04 |  633 |   3.5 |       4.3 | 0.7286373 | 0.378 |      0 |     9 |  2528 | 0.014302 |   50000 |
| 01:10:17 |  637 |  11.6 |       4.4 | 0.7271812 | 0.380 |      3 |     9 |  2544 | 0.004313 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.380 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.380 saved!
| 01:10:32 |  640 |  13.4 |       4.3 | 0.7260909 | 0.382 |      0 |     9 |  2556 | 0.003425 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.382 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.383 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.384 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:10:45 |  643 |   4.5 |       4.5 | 0.7250023 | 0.384 |      0 |     9 |  2568 | 0.003476 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.384 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_time_1745629850.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745629850.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.385 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:11:01 |  647 |   7.1 |       4.6 | 0.7235534 | 0.385 |      0 |     9 |  2584 | 0.004737 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.385 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
Attempting to save model to: /kaggle/working/models/pong_ep650.keras
✅ Model successfully saved to models/pong_ep650.keras (231.1 KB)
📊 Episode checkpoint saved at episode 650
| 01:11:12 |  652 |   7.3 |       4.5 | 0.7217463 | 0.385 |      0 |     9 |  2604 | 0.015612 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.386 saved!
| 01:11:25 |  656 |   4.7 |       4.5 | 0.7203039 | 0.386 |      0 |     9 |  2620 | 0.004846 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.386 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.386 saved!
| 01:11:37 |  661 |   3.7 |       4.3 | 0.7185050 | 0.385 |      0 |     9 |  2640 | 0.003971 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.387 saved!
| 01:11:50 |  663 |  14.1 |       4.5 | 0.7177866 | 0.389 |      0 |     9 |  2648 | 0.007187 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.389 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.390 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:12:03 |  668 |   4.1 |       4.6 | 0.7159940 | 0.389 |      0 |     9 |  2668 | 0.011294 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.390 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:12:20 |  671 |  14.3 |       4.7 | 0.7149205 | 0.392 |      0 |     9 |  2680 | 0.006058 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.392 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.393 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:12:32 |  674 |  11.4 |       4.9 | 0.7138487 | 0.395 |      3 |     9 |  2692 | 0.012496 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.395 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.395 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.395 saved!
| 01:12:49 |  678 |  15.8 |       4.9 | 0.7124220 | 0.398 |      5 |     9 |  2708 | 0.010531 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.398 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.399 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:12:59 |  680 |  11.2 |       5.1 | 0.7117098 | 0.401 |      9 |     9 |  2716 | 0.006072 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.401 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.402 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:13:11 |  684 |   1.3 |       4.9 | 0.7102875 | 0.401 |      0 |     9 |  2732 | 0.007141 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.402 saved!
| 01:13:24 |  686 |  16.8 |       5.1 | 0.7095773 | 0.405 |      7 |    10 |  2740 | 0.003573 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.405 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.405 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:13:34 |  688 |  10.6 |       5.2 | 0.7088679 | 0.407 |      0 |    10 |  2748 | 0.003110 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.407 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.407 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.407 saved!
| 01:13:44 |  693 |   1.2 |       5.1 | 0.7070975 | 0.406 |      0 |    10 |  2768 | 0.005433 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.409 saved!
| 01:13:59 |  695 |   8.1 |       5.1 | 0.7063906 | 0.409 |      0 |    10 |  2776 | 0.005405 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.409 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.412 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:14:15 |  697 |  10.7 |       5.4 | 0.7056844 | 0.413 |      0 |    10 |  2784 | 0.005258 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.413 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.413 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.413 saved!
| 01:14:28 |  700 |  11.6 |       5.4 | 0.7046264 | 0.415 |      3 |    10 |  2796 | 0.005118 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep700.keras
✅ Model successfully saved to models/pong_ep700.keras (231.1 KB)
📊 Episode checkpoint saved at episode 700
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.415 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:14:39 |  703 |  14.6 |       5.4 | 0.7035700 | 0.416 |      4 |    10 |  2808 | 0.001552 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.416 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.416 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.417 saved!
| 01:14:52 |  707 |   5.3 |       5.3 | 0.7021639 | 0.417 |      0 |    10 |  2824 | 0.001373 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.418 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.418 saved!
| 01:15:02 |  710 |   1.4 |       5.4 | 0.7011112 | 0.418 |      0 |    10 |  2836 | 0.006050 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.420 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.421 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:15:13 |  713 |   2.0 |       5.4 | 0.7000601 | 0.421 |      5 |    10 |  2848 | 0.004285 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.421 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.421 saved!
| 01:15:24 |  716 |   0.9 |       5.4 | 0.6990105 | 0.421 |      0 |    10 |  2860 | 0.009976 |   50000 |
| 01:15:36 |  720 |   7.4 |       5.3 | 0.6976135 | 0.421 |      0 |    10 |  2876 | 0.005261 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.422 saved!
| 01:15:49 |  723 |  13.8 |       5.3 | 0.6965676 | 0.423 |      0 |    10 |  2888 | 0.006310 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.423 saved!
✅ Model successfully force-saved to models/pong_time_1745630157.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745630157.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.426 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:16:05 |  726 |   8.6 |       5.6 | 0.6955233 | 0.427 |      0 |    11 |  2900 | 0.005911 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.427 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.428 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.428 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:16:16 |  730 |   0.1 |       5.6 | 0.6941333 | 0.427 |      0 |    11 |  2916 | 0.010159 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.429 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:16:31 |  732 |  13.9 |       5.8 | 0.6934393 | 0.431 |      0 |    11 |  2924 | 0.004900 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.431 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:16:49 |  737 |  18.4 |       5.9 | 0.6917075 | 0.432 |      5 |    11 |  2944 | 0.004746 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.432 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.432 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:17:00 |  739 |   8.9 |       5.9 | 0.6910159 | 0.433 |      0 |    11 |  2952 | 0.004567 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.433 saved!
| 01:17:15 |  744 |  10.4 |       5.7 | 0.6892901 | 0.433 |      0 |    11 |  2972 | 0.006215 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.433 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.434 saved!
| 01:17:28 |  747 |  10.9 |       5.7 | 0.6882567 | 0.435 |      3 |    11 |  2984 | 0.007806 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.435 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.436 saved!
| 01:17:39 |  750 |   0.4 |       5.9 | 0.6872248 | 0.435 |      0 |    11 |  2996 | 0.001341 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep750.keras
✅ Model successfully saved to models/pong_ep750.keras (231.1 KB)
📊 Episode checkpoint saved at episode 750
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.437 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:17:53 |  753 |   7.0 |       6.0 | 0.6861945 | 0.437 |      0 |    11 |  3008 | 0.005424 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.437 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.438 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:18:05 |  755 |   8.3 |       6.0 | 0.6855085 | 0.439 |      0 |    11 |  3016 | 0.003711 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.439 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.439 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.440 saved!
| 01:18:21 |  758 |   9.2 |       6.2 | 0.6844807 | 0.441 |      2 |    11 |  3028 | 0.007341 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.441 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:18:35 |  762 |  10.8 |       6.1 | 0.6831128 | 0.440 |      0 |    11 |  3044 | 0.003423 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.441 saved!
| 01:18:46 |  766 |   4.4 |       6.0 | 0.6817476 | 0.440 |      0 |    11 |  3060 | 0.009778 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.441 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.441 saved!
| 01:18:56 |  769 |   1.7 |       6.0 | 0.6807255 | 0.441 |      0 |    11 |  3072 | 0.001403 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.442 saved!
| 01:19:08 |  772 |   5.5 |       5.9 | 0.6797049 | 0.442 |      0 |    11 |  3084 | 0.001865 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.442 saved!
| 01:19:20 |  776 |   7.4 |       5.8 | 0.6783465 | 0.442 |      0 |    11 |  3100 | 0.009720 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.442 saved!
| 01:19:30 |  779 |   4.2 |       5.6 | 0.6773295 | 0.441 |      0 |    11 |  3112 | 0.002444 |   50000 |
| 01:19:43 |  783 |  10.5 |       5.6 | 0.6759759 | 0.442 |      0 |    11 |  3128 | 0.002160 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.442 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.442 saved!
| 01:19:55 |  785 |  10.6 |       5.6 | 0.6753001 | 0.443 |      0 |    11 |  3136 | 0.006733 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.443 saved!
| 01:20:09 |  788 |  11.1 |       5.5 | 0.6742876 | 0.444 |      0 |    11 |  3148 | 0.009650 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.444 saved!
| 01:20:23 |  794 |   8.0 |       5.3 | 0.6722673 | 0.443 |      0 |    11 |  3172 | 0.012212 |   50000 |
| 01:20:41 |  799 |  13.3 |       5.1 | 0.6705883 | 0.443 |      0 |    11 |  3192 | 0.006940 |   50000 |
| 01:20:52 |  800 |  16.9 |       5.1 | 0.6702530 | 0.445 |      5 |    11 |  3196 | 0.003490 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep800.keras
✅ Model successfully saved to models/pong_ep800.keras (231.1 KB)
📊 Episode checkpoint saved at episode 800
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.445 saved!
✅ Model successfully force-saved to models/pong_milestone_800.keras
🏆 Milestone save at episode 800
✅ Model successfully force-saved to models/pong_time_1745630459.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745630459.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.447 saved!
| 01:21:03 |  803 |   4.6 |       5.1 | 0.6692481 | 0.447 |      1 |    11 |  3208 | 0.012870 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.447 saved!
| 01:21:17 |  808 |   3.6 |       5.1 | 0.6675767 | 0.447 |      0 |    11 |  3228 | 0.004130 |   50000 |
| 01:21:32 |  812 |  14.8 |       5.0 | 0.6662425 | 0.448 |      4 |    11 |  3244 | 0.004711 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.448 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.448 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.449 saved!
| 01:21:49 |  815 |  14.4 |       5.1 | 0.6652437 | 0.451 |     11 |    11 |  3256 | 0.007197 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.451 saved!
| 01:22:02 |  818 |   8.6 |       5.2 | 0.6642463 | 0.451 |      2 |    11 |  3268 | 0.003021 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.451 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.452 saved!
| 01:22:14 |  821 |   1.4 |       5.2 | 0.6632504 | 0.452 |      0 |    11 |  3280 | 0.004707 |   50000 |
| 01:22:26 |  823 |  17.9 |       5.2 | 0.6625873 | 0.453 |      5 |    11 |  3288 | 0.002823 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.453 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.455 saved!
| 01:22:43 |  826 |   7.7 |       5.2 | 0.6615939 | 0.455 |      0 |    11 |  3300 | 0.001835 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.455 saved!
| 01:23:02 |  830 |  19.0 |       5.3 | 0.6602718 | 0.457 |      6 |    11 |  3316 | 0.010591 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.457 saved!
| 01:23:13 |  833 |   8.4 |       5.1 | 0.6592818 | 0.456 |      0 |    11 |  3328 | 0.003228 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.457 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.457 saved!
| 01:23:32 |  836 |  11.6 |       5.3 | 0.6582934 | 0.458 |      0 |    11 |  3340 | 0.004492 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.458 saved!
| 01:23:42 |  839 |   2.1 |       5.0 | 0.6573065 | 0.457 |      0 |    11 |  3352 | 0.004304 |   50000 |
| 01:23:53 |  844 |   1.9 |       4.9 | 0.6556648 | 0.456 |      0 |    11 |  3372 | 0.001135 |   50000 |
| 01:24:05 |  845 |  16.1 |       5.0 | 0.6553370 | 0.458 |      5 |    11 |  3376 | 0.003747 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.458 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.459 saved!
| 01:24:22 |  848 |   8.7 |       4.9 | 0.6543545 | 0.459 |      0 |    11 |  3388 | 0.005997 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.459 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.460 saved!
Attempting to save model to: /kaggle/working/models/pong_ep850.keras
✅ Model successfully saved to models/pong_ep850.keras (231.1 KB)
📊 Episode checkpoint saved at episode 850
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.460 saved!
| 01:24:36 |  851 |   8.3 |       5.1 | 0.6533735 | 0.461 |      0 |    11 |  3400 | 0.001183 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.461 saved!
| 01:24:46 |  852 |  16.9 |       5.2 | 0.6530468 | 0.463 |      5 |    11 |  3404 | 0.007193 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.463 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.464 saved!
| 01:24:57 |  854 |   4.7 |       5.1 | 0.6523939 | 0.464 |      0 |    11 |  3412 | 0.003531 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.464 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.464 saved!
| 01:25:12 |  856 |  16.1 |       5.2 | 0.6517417 | 0.466 |      5 |    11 |  3420 | 0.002130 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.466 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.466 saved!
| 01:25:23 |  859 |   6.9 |       5.2 | 0.6507645 | 0.467 |      0 |    11 |  3432 | 0.001951 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.467 saved!
| 01:25:35 |  861 |  19.3 |       5.3 | 0.6501139 | 0.469 |      6 |    11 |  3440 | 0.006726 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.469 saved!
| 01:25:52 |  864 |  21.1 |       5.4 | 0.6491392 | 0.471 |      6 |    11 |  3452 | 0.008243 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.471 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.471 saved!
| 01:26:05 |  867 |   8.4 |       5.5 | 0.6481660 | 0.471 |      0 |    11 |  3464 | 0.000649 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745630765.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745630765.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.471 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.472 saved!
| 01:26:16 |  870 |   0.2 |       5.5 | 0.6471943 | 0.471 |      0 |    11 |  3476 | 0.009077 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.473 saved!
| 01:26:26 |  872 |   1.2 |       5.5 | 0.6465472 | 0.472 |      0 |    11 |  3484 | 0.003747 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.474 saved!
| 01:26:40 |  874 |  10.8 |       5.7 | 0.6459008 | 0.474 |      0 |    11 |  3492 | 0.004989 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.474 saved!
| 01:26:56 |  877 |  16.9 |       5.8 | 0.6449325 | 0.476 |      5 |    11 |  3504 | 0.010536 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.476 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.476 saved!
| 01:27:13 |  879 |  16.4 |       6.0 | 0.6442877 | 0.478 |      5 |    11 |  3512 | 0.003107 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.478 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.478 saved!
| 01:27:29 |  881 |  17.3 |       6.2 | 0.6436436 | 0.480 |      5 |    11 |  3520 | 0.004875 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.480 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:27:40 |  882 |  17.6 |       6.4 | 0.6433218 | 0.482 |     10 |    11 |  3524 | 0.000332 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.482 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:27:50 |  886 |   1.6 |       6.2 | 0.6420361 | 0.481 |      0 |    11 |  3540 | 0.003113 |   50000 |
| 01:28:04 |  888 |  12.6 |       6.2 | 0.6413942 | 0.482 |      0 |    11 |  3548 | 0.002159 |   50000 |
| 01:28:20 |  891 |  15.6 |       6.3 | 0.6404326 | 0.482 |      0 |    11 |  3560 | 0.003708 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.482 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:28:38 |  895 |   9.1 |       6.4 | 0.6391527 | 0.482 |      0 |    11 |  3576 | 0.001491 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:28:49 |  898 |   4.4 |       6.5 | 0.6381944 | 0.482 |      1 |    11 |  3588 | 0.004527 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.482 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
Attempting to save model to: /kaggle/working/models/pong_ep900.keras
✅ Model successfully saved to models/pong_ep900.keras (231.1 KB)
📊 Episode checkpoint saved at episode 900
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.483 saved!
| 01:29:05 |  901 |  11.2 |       6.3 | 0.6372376 | 0.484 |      0 |    11 |  3600 | 0.003587 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.484 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.484 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.484 saved!
| 01:29:22 |  904 |  11.4 |       6.5 | 0.6362822 | 0.485 |      0 |    11 |  3612 | 0.008747 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.485 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.485 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:29:33 |  906 |  10.0 |       6.6 | 0.6356461 | 0.486 |      2 |    11 |  3620 | 0.006238 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.486 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:29:43 |  908 |  11.0 |       6.6 | 0.6350106 | 0.486 |      0 |    11 |  3628 | 0.002000 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.486 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.486 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:29:55 |  910 |   7.6 |       6.6 | 0.6343758 | 0.486 |      0 |    11 |  3636 | 0.007384 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.486 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:30:07 |  911 |  15.9 |       6.8 | 0.6340586 | 0.488 |      5 |    11 |  3640 | 0.004615 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.488 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.488 saved!
| 01:30:26 |  915 |  17.5 |       6.7 | 0.6327914 | 0.490 |      5 |    11 |  3656 | 0.003272 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.490 saved!
| 01:30:37 |  917 |  19.3 |       6.8 | 0.6321588 | 0.491 |      5 |    11 |  3664 | 0.008779 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.491 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.492 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:30:49 |  919 |   6.0 |       6.9 | 0.6315268 | 0.492 |      9 |    11 |  3672 | 0.001619 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.492 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.493 saved!
| 01:31:02 |  921 |  15.0 |       7.0 | 0.6308954 | 0.494 |      0 |    11 |  3680 | 0.004739 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.494 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_time_1745631068.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745631068.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.494 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:31:20 |  923 |  17.1 |       7.0 | 0.6302647 | 0.496 |      7 |    11 |  3688 | 0.007591 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.496 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.496 saved!
| 01:31:31 |  925 |   2.0 |       7.0 | 0.6296346 | 0.496 |      0 |    11 |  3696 | 0.004261 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.496 saved!
| 01:31:44 |  927 |   7.7 |       7.1 | 0.6290051 | 0.497 |      0 |    11 |  3704 | 0.006122 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.497 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.497 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:31:55 |  930 |   4.4 |       6.9 | 0.6280621 | 0.497 |      0 |    11 |  3716 | 0.005589 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.497 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.497 saved!
| 01:32:11 |  934 |  11.6 |       6.9 | 0.6268069 | 0.497 |      0 |    11 |  3732 | 0.002625 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.497 saved!
| 01:32:21 |  935 |  18.6 |       7.1 | 0.6264935 | 0.499 |      5 |    11 |  3736 | 0.008257 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.499 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.499 saved!
| 01:32:33 |  937 |  12.0 |       7.1 | 0.6258671 | 0.500 |      3 |    11 |  3744 | 0.002098 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.500 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.501 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:32:49 |  939 |  15.7 |       7.3 | 0.6252414 | 0.502 |     10 |    11 |  3752 | 0.001510 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.502 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.503 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:33:00 |  941 |   9.7 |       7.5 | 0.6246163 | 0.503 |     14 |    11 |  3760 | 0.000511 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.503 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:33:15 |  944 |  18.4 |       7.7 | 0.6236799 | 0.505 |      6 |    11 |  3772 | 0.003879 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.505 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.506 saved!
| 01:33:26 |  947 |   0.7 |       7.6 | 0.6227448 | 0.505 |      0 |    11 |  3784 | 0.000392 |   50000 |
| 01:33:38 |  948 |  16.8 |       7.6 | 0.6224335 | 0.507 |      5 |    11 |  3788 | 0.001819 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.507 saved!
| 01:33:50 |  949 |  16.1 |       7.7 | 0.6221222 | 0.508 |     10 |    11 |  3792 | 0.012845 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.508 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:34:02 |  950 |  16.5 |       7.8 | 0.6218112 | 0.510 |     15 |    11 |  3796 | 0.002002 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep950.keras
✅ Model successfully saved to models/pong_ep950.keras (231.1 KB)
📊 Episode checkpoint saved at episode 950
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.510 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:34:17 |  952 |  18.0 |       7.8 | 0.6211895 | 0.511 |      5 |    11 |  3804 | 0.004471 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.511 saved!
| 01:34:30 |  954 |  16.5 |       7.8 | 0.6205685 | 0.512 |      4 |    11 |  3812 | 0.006072 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.512 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.512 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:34:49 |  957 |  13.0 |       7.8 | 0.6196381 | 0.513 |      3 |    11 |  3824 | 0.001235 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.513 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.514 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:35:11 |  959 |  12.8 |       8.0 | 0.6190186 | 0.515 |      4 |    11 |  3832 | 0.004298 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.515 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.515 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:35:30 |  961 |  15.2 |       8.0 | 0.6183998 | 0.516 |      0 |    11 |  3840 | 0.005826 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.516 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.517 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:35:42 |  964 |   7.4 |       7.9 | 0.6174726 | 0.517 |      0 |    11 |  3852 | 0.004295 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.517 saved!
| 01:35:53 |  968 |   4.4 |       7.9 | 0.6162386 | 0.516 |      1 |    11 |  3868 | 0.006503 |   50000 |
| 01:36:03 |  969 |  15.1 |       7.9 | 0.6159305 | 0.517 |      5 |    11 |  3872 | 0.000747 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.517 saved!
| 01:36:15 |  971 |  14.2 |       7.9 | 0.6153147 | 0.518 |      4 |    11 |  3880 | 0.004359 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745631375.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745631375.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.518 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.519 saved!
| 01:36:33 |  973 |  15.8 |       8.0 | 0.6146996 | 0.520 |     11 |    11 |  3888 | 0.008044 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.520 saved!
| 01:36:44 |  975 |  12.5 |       8.0 | 0.6140850 | 0.521 |      3 |    11 |  3896 | 0.002325 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.521 saved!
| 01:36:56 |  977 |  13.7 |       8.0 | 0.6134711 | 0.522 |      0 |    11 |  3904 | 0.000708 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.522 saved!
| 01:37:07 |  979 |   8.0 |       7.8 | 0.6128578 | 0.522 |      0 |    11 |  3912 | 0.001554 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.522 saved!
| 01:37:19 |  980 |  16.5 |       8.0 | 0.6125513 | 0.523 |      5 |    11 |  3916 | 0.002762 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.523 saved!
| 01:37:33 |  983 |   5.5 |       7.7 | 0.6116330 | 0.524 |      1 |    11 |  3928 | 0.001125 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.524 saved!
| 01:37:43 |  984 |  15.8 |       7.9 | 0.6113271 | 0.525 |      0 |    11 |  3932 | 0.002002 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.525 saved!
| 01:37:56 |  985 |  19.0 |       8.0 | 0.6110215 | 0.526 |      6 |    11 |  3936 | 0.003498 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.526 saved!
| 01:38:08 |  986 |  16.8 |       8.2 | 0.6107160 | 0.528 |     11 |    11 |  3940 | 0.004841 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.528 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:38:20 |  988 |  16.1 |       8.2 | 0.6101054 | 0.528 |      4 |    11 |  3948 | 0.006293 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.528 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.530 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:38:33 |  990 |   6.1 |       8.4 | 0.6094955 | 0.530 |      9 |    11 |  3956 | 0.004930 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.530 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.530 saved!
| 01:38:54 |  992 |  17.6 |       8.5 | 0.6088861 | 0.532 |      5 |    11 |  3964 | 0.005793 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.532 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.532 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:39:06 |  995 |   4.9 |       8.5 | 0.6079732 | 0.532 |      1 |    11 |  3976 | 0.001350 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.532 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:39:24 |  997 |  14.1 |       8.6 | 0.6073654 | 0.533 |      0 |    11 |  3984 | 0.012705 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.533 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.533 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:39:36 |  999 |   6.9 |       8.7 | 0.6067582 | 0.533 |      0 |    11 |  3992 | 0.005597 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.533 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
Attempting to save model to: /kaggle/working/models/pong_ep1000.keras
✅ Model successfully saved to models/pong_ep1000.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1000
✅ Model successfully force-saved to models/pong_milestone_1000.keras
🏆 Milestone save at episode 1000
| 01:39:54 | 1002 |   8.7 |       8.6 | 0.6058485 | 0.533 |      0 |    11 |  4004 | 0.004363 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.533 saved!
| 01:40:07 | 1004 |  13.9 |       8.6 | 0.6052428 | 0.534 |      4 |    11 |  4012 | 0.004879 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.534 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.534 saved!
| 01:40:17 | 1006 |   1.6 |       8.5 | 0.6046377 | 0.534 |      0 |    11 |  4020 | 0.002457 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.535 saved!
| 01:40:30 | 1008 |   5.0 |       8.6 | 0.6040332 | 0.535 |      0 |    11 |  4028 | 0.008092 |   50000 |
| 01:40:46 | 1010 |  14.6 |       8.6 | 0.6034294 | 0.536 |      5 |    11 |  4036 | 0.001950 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.536 saved!
| 01:40:56 | 1011 |  15.5 |       8.6 | 0.6031276 | 0.537 |      0 |    11 |  4040 | 0.001742 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.537 saved!
| 01:41:08 | 1012 |  16.5 |       8.7 | 0.6028261 | 0.538 |      5 |    11 |  4044 | 0.004509 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.538 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_time_1745631676.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745631676.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.539 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:41:22 | 1014 |   8.0 |       8.9 | 0.6022234 | 0.539 |      0 |    11 |  4052 | 0.003936 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.539 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:41:33 | 1016 |  15.1 |       8.9 | 0.6016213 | 0.540 |      4 |    11 |  4060 | 0.007281 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.540 saved!
| 01:41:45 | 1018 |  11.8 |       8.7 | 0.6010199 | 0.540 |      0 |    11 |  4068 | 0.002774 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.540 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.540 saved!
| 01:42:00 | 1020 |  17.8 |       8.8 | 0.6004190 | 0.541 |      6 |    11 |  4076 | 0.005438 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.541 saved!
| 01:42:11 | 1021 |  17.5 |       8.8 | 0.6001188 | 0.542 |     10 |    11 |  4080 | 0.007859 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.542 saved!
| 01:42:22 | 1022 |  15.3 |       8.9 | 0.5998187 | 0.543 |      0 |    11 |  4084 | 0.003607 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.543 saved!
| 01:42:36 | 1023 |  16.0 |       8.9 | 0.5995188 | 0.544 |      5 |    11 |  4088 | 0.004460 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.544 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.544 saved!
| 01:42:47 | 1025 |  11.1 |       9.0 | 0.5989194 | 0.545 |      0 |    11 |  4096 | 0.007986 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.545 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:43:05 | 1027 |  16.4 |       9.0 | 0.5983207 | 0.546 |      5 |    11 |  4104 | 0.000700 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.546 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:43:19 | 1028 |  17.2 |       9.1 | 0.5980215 | 0.547 |     10 |    11 |  4108 | 0.003087 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.547 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.548 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:43:31 | 1031 |   1.4 |       9.1 | 0.5971249 | 0.547 |      0 |    11 |  4120 | 0.000413 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:43:43 | 1034 |   5.1 |       9.1 | 0.5962297 | 0.547 |      0 |    11 |  4132 | 0.000704 |   50000 |
| 01:43:55 | 1036 |   7.9 |       9.0 | 0.5956336 | 0.547 |      0 |    11 |  4140 | 0.004037 |   50000 |
| 01:44:16 | 1038 |  16.0 |       9.0 | 0.5950381 | 0.548 |      5 |    11 |  4148 | 0.001342 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.548 saved!
| 01:44:29 | 1040 |  11.0 |       8.9 | 0.5944432 | 0.549 |      0 |    11 |  4156 | 0.000982 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.549 saved!
| 01:44:50 | 1043 |  19.8 |       9.0 | 0.5935520 | 0.550 |      6 |    11 |  4168 | 0.001266 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.550 saved!
| 01:45:00 | 1044 |  15.2 |       9.0 | 0.5932552 | 0.551 |      0 |    11 |  4172 | 0.001654 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.551 saved!
| 01:45:14 | 1045 |  16.5 |       9.0 | 0.5929586 | 0.552 |      5 |    11 |  4176 | 0.011228 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.552 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.552 saved!
| 01:45:32 | 1047 |  12.7 |       9.3 | 0.5923658 | 0.553 |     11 |    11 |  4184 | 0.010300 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.553 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.554 saved!
| 01:45:53 | 1050 |  16.7 |       9.1 | 0.5914777 | 0.555 |      8 |    11 |  4196 | 0.005416 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1050.keras
✅ Model successfully saved to models/pong_ep1050.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1050
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.555 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.555 saved!
| 01:46:10 | 1052 |  14.3 |       9.1 | 0.5908864 | 0.556 |      0 |    11 |  4204 | 0.001165 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.556 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.556 saved!
✅ Model successfully force-saved to models/pong_time_1745631980.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745631980.keras
| 01:46:25 | 1056 |   8.0 |       8.9 | 0.5897055 | 0.556 |      2 |    11 |  4220 | 0.001827 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.556 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.557 saved!
| 01:46:45 | 1058 |  16.1 |       9.0 | 0.5891159 | 0.558 |     10 |    11 |  4228 | 0.000564 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.558 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.559 saved!
| 01:47:00 | 1060 |   9.5 |       9.0 | 0.5885270 | 0.559 |     16 |    11 |  4236 | 0.001506 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.559 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.559 saved!
| 01:47:18 | 1062 |  15.9 |       9.0 | 0.5879386 | 0.560 |     21 |    11 |  4244 | 0.000815 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.560 saved!
| 01:47:33 | 1064 |  14.2 |       9.0 | 0.5873508 | 0.561 |      4 |    11 |  4252 | 0.004528 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.561 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.561 saved!
| 01:47:56 | 1066 |  14.3 |       9.3 | 0.5867636 | 0.562 |      4 |    11 |  4260 | 0.006800 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.562 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.563 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:48:10 | 1068 |   4.8 |       9.4 | 0.5861770 | 0.563 |      0 |    11 |  4268 | 0.001449 |   50000 |
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.563 saved!
| 01:48:23 | 1071 |   2.0 |       9.2 | 0.5852981 | 0.562 |      0 |    11 |  4280 | 0.002546 |   50000 |
| 01:48:36 | 1072 |  14.8 |       9.2 | 0.5850055 | 0.563 |      0 |    11 |  4284 | 0.001702 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.563 saved!
| 01:48:48 | 1073 |  17.8 |       9.3 | 0.5847130 | 0.564 |      5 |    11 |  4288 | 0.006966 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.564 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.564 saved!
| 01:49:12 | 1076 |  20.0 |       9.4 | 0.5838364 | 0.566 |      7 |    11 |  4300 | 0.000804 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.566 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:49:26 | 1077 |  18.0 |       9.4 | 0.5835444 | 0.567 |     12 |    11 |  4304 | 0.000801 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.567 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:49:39 | 1078 |  17.1 |       9.6 | 0.5832527 | 0.568 |     17 |    11 |  4308 | 0.005738 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.568 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.568 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 01:49:51 | 1080 |   1.5 |       9.5 | 0.5826696 | 0.568 |      0 |    11 |  4316 | 0.003353 |   50000 |
| 01:50:11 | 1083 |  14.5 |       9.6 | 0.5817960 | 0.569 |      4 |    11 |  4328 | 0.003918 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.569 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.569 saved!
| 01:50:22 | 1087 |   3.8 |       9.2 | 0.5806333 | 0.568 |      0 |    11 |  4344 | 0.001065 |   50000 |
| 01:50:32 | 1089 |   7.7 |       9.0 | 0.5800528 | 0.568 |      0 |    11 |  4352 | 0.000508 |   50000 |
| 01:50:46 | 1091 |  16.6 |       9.0 | 0.5794729 | 0.569 |      0 |    11 |  4360 | 0.001013 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.569 saved!
| 01:50:58 | 1092 |  13.9 |       8.9 | 0.5791831 | 0.570 |      4 |    11 |  4364 | 0.000996 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.570 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.570 saved!
| 01:51:14 | 1095 |   8.0 |       9.0 | 0.5783148 | 0.570 |      3 |    11 |  4376 | 0.004822 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.570 saved!
| 01:51:27 | 1096 |  15.9 |       9.1 | 0.5780256 | 0.571 |      8 |    11 |  4380 | 0.002795 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745632287.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745632287.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.571 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.572 saved!
| 01:51:47 | 1099 |  14.7 |       9.0 | 0.5771590 | 0.572 |      4 |    11 |  4392 | 0.000631 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.572 saved!
Attempting to save model to: /kaggle/working/models/pong_ep1100.keras
✅ Model successfully saved to models/pong_ep1100.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1100
| 01:52:04 | 1101 |  17.2 |       9.1 | 0.5765820 | 0.573 |      5 |    11 |  4400 | 0.000439 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.573 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.573 saved!
| 01:52:21 | 1103 |  18.1 |       9.3 | 0.5760056 | 0.574 |      5 |    11 |  4408 | 0.006844 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.574 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.575 saved!
| 01:52:34 | 1105 |   5.5 |       9.2 | 0.5754297 | 0.575 |      1 |    11 |  4416 | 0.009533 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.575 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.575 saved!
| 01:52:45 | 1107 |   1.5 |       9.2 | 0.5748544 | 0.575 |      0 |    11 |  4424 | 0.000452 |   50000 |
| 01:53:02 | 1109 |  14.7 |       9.3 | 0.5742797 | 0.576 |      4 |    11 |  4432 | 0.000374 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.576 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.576 saved!
| 01:53:13 | 1111 |   2.0 |       9.1 | 0.5737056 | 0.576 |      0 |    11 |  4440 | 0.000960 |   50000 |
| 01:53:26 | 1112 |  13.8 |       9.1 | 0.5734187 | 0.577 |      0 |    11 |  4444 | 0.000504 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.577 saved!
| 01:53:46 | 1115 |  19.7 |       9.1 | 0.5725590 | 0.578 |      7 |    12 |  4456 | 0.001493 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.578 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.578 saved!
| 01:54:08 | 1117 |  16.6 |       9.3 | 0.5719866 | 0.579 |     15 |    12 |  4464 | 0.000849 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.579 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.579 saved!
| 01:54:18 | 1120 |   0.1 |       9.0 | 0.5711291 | 0.579 |      0 |    12 |  4476 | 0.001536 |   50000 |
| 01:54:32 | 1121 |  17.7 |       9.0 | 0.5708435 | 0.580 |      5 |    12 |  4480 | 0.000706 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.580 saved!
| 01:54:44 | 1122 |  17.4 |       9.0 | 0.5705581 | 0.581 |     10 |    12 |  4484 | 0.003915 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.581 saved!
| 01:54:59 | 1124 |  18.0 |       9.0 | 0.5699877 | 0.582 |      5 |    12 |  4492 | 0.005828 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.582 saved!
| 01:55:15 | 1126 |  10.8 |       9.0 | 0.5694178 | 0.582 |      0 |    12 |  4500 | 0.001197 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.582 saved!
| 01:55:25 | 1127 |  14.1 |       9.0 | 0.5691331 | 0.583 |      3 |    12 |  4504 | 0.011089 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.583 saved!
| 01:55:38 | 1128 |  15.3 |       9.0 | 0.5688486 | 0.583 |      0 |    12 |  4508 | 0.001128 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.583 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.583 saved!
| 01:55:52 | 1130 |   5.6 |       9.0 | 0.5682798 | 0.584 |      1 |    12 |  4516 | 0.004402 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.584 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.584 saved!
| 01:56:10 | 1132 |  18.5 |       9.3 | 0.5677117 | 0.585 |      8 |    12 |  4524 | 0.006573 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.585 saved!
| 01:56:22 | 1136 |   2.0 |       9.2 | 0.5665771 | 0.585 |      0 |    12 |  4540 | 0.000317 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745632590.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745632590.keras
| 01:56:38 | 1138 |  11.6 |       9.1 | 0.5660107 | 0.585 |      3 |    12 |  4548 | 0.000871 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.585 saved!
| 01:56:52 | 1140 |  16.9 |       9.2 | 0.5654448 | 0.586 |      0 |    12 |  4556 | 0.003938 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.586 saved!
| 01:57:04 | 1141 |  19.9 |       9.4 | 0.5651621 | 0.587 |      6 |    12 |  4560 | 0.000594 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.587 saved!
| 01:57:16 | 1142 |  11.6 |       9.4 | 0.5648795 | 0.587 |      0 |    12 |  4564 | 0.001163 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.587 saved!
| 01:57:27 | 1143 |  15.4 |       9.3 | 0.5645971 | 0.588 |      4 |    12 |  4568 | 0.007351 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.588 saved!
| 01:57:39 | 1146 |   5.0 |       9.0 | 0.5637506 | 0.588 |      1 |    12 |  4580 | 0.005378 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.588 saved!
| 01:57:52 | 1148 |  10.4 |       9.0 | 0.5631870 | 0.588 |      0 |    12 |  4588 | 0.000634 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.588 saved!
Attempting to save model to: /kaggle/working/models/pong_ep1150.keras
✅ Model successfully saved to models/pong_ep1150.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1150
| 01:58:03 | 1151 |   4.0 |       8.8 | 0.5623426 | 0.588 |      0 |    12 |  4600 | 0.001911 |   50000 |
| 01:58:20 | 1153 |  10.7 |       8.8 | 0.5617804 | 0.588 |      0 |    12 |  4608 | 0.001455 |   50000 |
| 01:58:34 | 1156 |  15.5 |       8.8 | 0.5609382 | 0.588 |      4 |    12 |  4620 | 0.001590 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.588 saved!
| 01:58:53 | 1158 |  17.9 |       8.8 | 0.5603774 | 0.589 |      5 |    12 |  4628 | 0.005685 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.589 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.589 saved!
| 01:59:08 | 1161 |  10.2 |       8.6 | 0.5595373 | 0.589 |      0 |    12 |  4640 | 0.000895 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.589 saved!
| 01:59:23 | 1163 |  10.6 |       8.6 | 0.5589779 | 0.590 |      0 |    12 |  4648 | 0.000467 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.590 saved!
| 01:59:38 | 1165 |  14.4 |       8.5 | 0.5584190 | 0.590 |      0 |    12 |  4656 | 0.001481 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.590 saved!
| 01:59:52 | 1166 |  18.1 |       8.6 | 0.5581398 | 0.591 |      6 |    12 |  4660 | 0.000966 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.591 saved!
| 02:00:11 | 1168 |  17.5 |       8.6 | 0.5575818 | 0.592 |      5 |    12 |  4668 | 0.001003 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.592 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.592 saved!
| 02:00:28 | 1170 |  15.3 |       8.7 | 0.5570244 | 0.592 |      0 |    12 |  4676 | 0.000511 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.592 saved!
| 02:00:43 | 1171 |  18.7 |       8.9 | 0.5567459 | 0.593 |      5 |    12 |  4680 | 0.000234 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.593 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.594 saved!
| 02:01:03 | 1174 |  18.1 |       8.8 | 0.5559112 | 0.594 |      5 |    12 |  4692 | 0.000636 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.594 saved!
| 02:01:17 | 1175 |  19.6 |       8.9 | 0.5556332 | 0.595 |     10 |    12 |  4696 | 0.000265 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.595 saved!
| 02:01:31 | 1176 |  18.2 |       8.9 | 0.5553554 | 0.596 |     15 |    12 |  4700 | 0.000851 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745632891.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745632891.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.596 saved!
| 02:01:50 | 1180 |  11.9 |       8.6 | 0.5542455 | 0.596 |      3 |    12 |  4716 | 0.002067 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.596 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.596 saved!
| 02:02:03 | 1183 |   6.1 |       8.5 | 0.5534145 | 0.597 |      6 |    12 |  4728 | 0.001063 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.597 saved!
| 02:02:15 | 1186 |  11.3 |       8.6 | 0.5525848 | 0.597 |      3 |    12 |  4740 | 0.000688 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.597 saved!
| 02:02:32 | 1189 |  20.4 |       8.6 | 0.5517564 | 0.598 |      6 |    12 |  4752 | 0.006728 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.598 saved!
| 02:02:46 | 1191 |  11.4 |       8.6 | 0.5512048 | 0.598 |      0 |    12 |  4760 | 0.007443 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.598 saved!
| 02:03:00 | 1192 |  17.1 |       8.6 | 0.5509292 | 0.599 |      5 |    12 |  4764 | 0.005706 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.599 saved!
| 02:03:10 | 1193 |  14.3 |       8.7 | 0.5506537 | 0.599 |      0 |    12 |  4768 | 0.003719 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.599 saved!
| 02:03:28 | 1196 |  14.7 |       8.6 | 0.5498281 | 0.599 |      0 |    12 |  4780 | 0.005333 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.599 saved!
| 02:03:42 | 1197 |  19.9 |       8.8 | 0.5495532 | 0.600 |      6 |    12 |  4784 | 0.000346 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.600 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.601 saved!
| 02:03:53 | 1199 |   7.4 |       8.7 | 0.5490038 | 0.601 |      0 |    12 |  4792 | 0.000340 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.601 saved!
Attempting to save model to: /kaggle/working/models/pong_ep1200.keras
✅ Model successfully saved to models/pong_ep1200.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1200
✅ Model successfully force-saved to models/pong_milestone_1200.keras
🏆 Milestone save at episode 1200
| 02:04:09 | 1201 |  17.2 |       8.7 | 0.5484549 | 0.601 |      5 |    12 |  4800 | 0.001084 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.601 saved!
| 02:04:21 | 1204 |  10.1 |       8.4 | 0.5476327 | 0.601 |      2 |    12 |  4812 | 0.000476 |   50000 |
| 02:04:32 | 1205 |  14.8 |       8.5 | 0.5473588 | 0.602 |      6 |    12 |  4816 | 0.000559 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.602 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.602 saved!
| 02:04:52 | 1209 |  16.7 |       8.5 | 0.5462649 | 0.603 |     12 |    12 |  4832 | 0.000779 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.603 saved!
| 02:05:08 | 1212 |  18.3 |       8.4 | 0.5454460 | 0.603 |      5 |    12 |  4844 | 0.000478 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.603 saved!
| 02:05:23 | 1215 |   9.2 |       8.3 | 0.5446282 | 0.603 |      2 |    12 |  4856 | 0.001032 |   50000 |
| 02:05:34 | 1216 |  12.3 |       8.3 | 0.5443559 | 0.604 |      5 |    12 |  4860 | 0.000641 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.604 saved!
| 02:05:49 | 1217 |  19.8 |       8.4 | 0.5440837 | 0.605 |     11 |    12 |  4864 | 0.000498 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.605 saved!
| 02:06:04 | 1218 |  16.8 |       8.5 | 0.5438117 | 0.605 |     16 |    12 |  4868 | 0.005515 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.605 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.605 saved!
| 02:06:20 | 1220 |  12.1 |       8.6 | 0.5432680 | 0.606 |      3 |    12 |  4876 | 0.000370 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.606 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.606 saved!
| 02:06:35 | 1222 |   8.8 |       8.4 | 0.5427249 | 0.606 |      0 |    12 |  4884 | 0.000933 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745633195.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745633195.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.606 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.606 saved!
| 02:06:56 | 1224 |  17.5 |       8.5 | 0.5421823 | 0.607 |      5 |    12 |  4892 | 0.000393 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.607 saved!
| 02:07:09 | 1225 |  17.4 |       8.6 | 0.5419112 | 0.608 |     10 |    12 |  4896 | 0.000888 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.608 saved!
| 02:07:22 | 1226 |  18.6 |       8.7 | 0.5416402 | 0.609 |     15 |    12 |  4900 | 0.006849 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.609 saved!
| 02:07:36 | 1227 |  18.1 |       8.7 | 0.5413694 | 0.609 |     20 |    12 |  4904 | 0.001753 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.609 saved!
| 02:07:47 | 1228 |  13.1 |       8.7 | 0.5410987 | 0.610 |     23 |    12 |  4908 | 0.000884 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.610 saved!
| 02:08:02 | 1229 |  17.9 |       8.8 | 0.5408282 | 0.611 |     28 |    12 |  4912 | 0.000628 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.611 saved!
| 02:08:13 | 1230 |  11.8 |       8.9 | 0.5405578 | 0.611 |      0 |    12 |  4916 | 0.011880 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.611 saved!
| 02:08:27 | 1231 |  19.0 |       9.0 | 0.5402875 | 0.612 |      6 |    12 |  4920 | 0.005018 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.612 saved!
| 02:08:40 | 1232 |  15.8 |       9.0 | 0.5400173 | 0.613 |     10 |    12 |  4924 | 0.005536 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.613 saved!
| 02:08:53 | 1233 |  17.0 |       9.1 | 0.5397473 | 0.613 |     15 |    12 |  4928 | 0.005503 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.613 saved!
| 02:09:05 | 1234 |  15.3 |       9.2 | 0.5394774 | 0.614 |      0 |    12 |  4932 | 0.005603 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.614 saved!
| 02:09:19 | 1235 |  14.0 |       9.3 | 0.5392077 | 0.614 |      4 |    12 |  4936 | 0.001308 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.614 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.615 saved!
| 02:09:33 | 1237 |   7.0 |       9.4 | 0.5386686 | 0.615 |      0 |    12 |  4944 | 0.000570 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.615 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.615 saved!
| 02:09:52 | 1239 |  16.3 |       9.5 | 0.5381301 | 0.616 |      6 |    12 |  4952 | 0.006966 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.616 saved!
| 02:10:04 | 1241 |   8.6 |       9.2 | 0.5375921 | 0.615 |      0 |    12 |  4960 | 0.003936 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.616 saved!
| 02:10:19 | 1243 |   7.9 |       9.1 | 0.5370546 | 0.616 |      5 |    12 |  4968 | 0.005045 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.616 saved!
| 02:10:32 | 1244 |  16.0 |       9.3 | 0.5367861 | 0.617 |     10 |    12 |  4972 | 0.004882 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.617 saved!
| 02:10:47 | 1245 |  15.9 |       9.4 | 0.5365177 | 0.618 |     15 |    12 |  4976 | 0.010703 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.618 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.618 saved!
| 02:10:59 | 1247 |   4.3 |       9.4 | 0.5359813 | 0.618 |      0 |    12 |  4984 | 0.006627 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.618 saved!
| 02:11:13 | 1249 |   8.8 |       9.5 | 0.5354455 | 0.618 |      4 |    12 |  4992 | 0.003986 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.618 saved!
Attempting to save model to: /kaggle/working/models/pong_ep1250.keras
✅ Model successfully saved to models/pong_ep1250.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1250
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.618 saved!
| 02:11:38 | 1251 |  17.8 |       9.7 | 0.5349102 | 0.619 |      0 |    12 |  5000 | 0.001713 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745633498.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745633498.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.619 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.619 saved!
| 02:11:53 | 1254 |   5.6 |       9.6 | 0.5341082 | 0.619 |      3 |    12 |  5012 | 0.006371 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.619 saved!
| 02:12:07 | 1255 |  16.3 |       9.8 | 0.5338412 | 0.620 |      8 |    12 |  5016 | 0.001121 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.620 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.620 saved!
| 02:12:20 | 1257 |   4.0 |       9.7 | 0.5333075 | 0.620 |      0 |    12 |  5024 | 0.000689 |   50000 |
| 02:12:35 | 1258 |  17.1 |       9.7 | 0.5330408 | 0.621 |      5 |    12 |  5028 | 0.000756 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.621 saved!
| 02:12:45 | 1259 |  11.1 |       9.7 | 0.5327743 | 0.621 |      0 |    12 |  5032 | 0.000576 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.621 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.621 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.621 saved!
| 02:13:04 | 1262 |  13.0 |       9.8 | 0.5319755 | 0.622 |      6 |    12 |  5044 | 0.000370 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.622 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:13:18 | 1263 |  21.0 |       9.9 | 0.5317095 | 0.623 |     12 |    12 |  5048 | 0.000503 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.623 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:13:37 | 1265 |  12.0 |       9.9 | 0.5311780 | 0.623 |      4 |    12 |  5056 | 0.000828 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.623 saved!
| 02:13:48 | 1266 |  13.3 |       9.9 | 0.5309124 | 0.624 |      7 |    12 |  5060 | 0.009608 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.624 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.624 saved!
| 02:14:00 | 1268 |   5.3 |       9.8 | 0.5303816 | 0.624 |      0 |    12 |  5068 | 0.000910 |   50000 |
| 02:14:12 | 1269 |  15.0 |       9.9 | 0.5301164 | 0.624 |      4 |    12 |  5072 | 0.000554 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.624 saved!
| 02:14:29 | 1271 |  17.8 |       9.7 | 0.5295864 | 0.625 |      5 |    12 |  5080 | 0.000539 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.625 saved!
| 02:14:44 | 1272 |  17.4 |       9.9 | 0.5293216 | 0.626 |     10 |    12 |  5084 | 0.003856 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.626 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.626 saved!
| 02:15:06 | 1275 |  19.7 |       9.7 | 0.5285280 | 0.627 |      6 |    12 |  5096 | 0.000992 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.627 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.627 saved!
| 02:15:27 | 1278 |  14.7 |       9.7 | 0.5277356 | 0.627 |      0 |    12 |  5108 | 0.001164 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.627 saved!
| 02:15:42 | 1279 |  17.7 |       9.9 | 0.5274718 | 0.628 |      5 |    12 |  5112 | 0.000926 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.628 saved!
| 02:15:57 | 1281 |  15.3 |       9.9 | 0.5269444 | 0.628 |      4 |    12 |  5120 | 0.001426 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.628 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.628 saved!
| 02:16:19 | 1283 |  15.7 |      10.0 | 0.5264176 | 0.629 |      9 |    12 |  5128 | 0.000814 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.629 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.629 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:16:38 | 1285 |  18.2 |      10.2 | 0.5258913 | 0.630 |     16 |    12 |  5136 | 0.000437 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.630 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:16:52 | 1286 |  19.8 |      10.3 | 0.5256284 | 0.631 |     22 |    12 |  5140 | 0.001010 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745633812.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745633812.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.631 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:17:07 | 1287 |  18.6 |      10.5 | 0.5253656 | 0.631 |     28 |    12 |  5144 | 0.000867 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.631 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:17:21 | 1288 |  15.5 |      10.6 | 0.5251029 | 0.632 |     32 |    12 |  5148 | 0.000356 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.632 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:17:32 | 1289 |  15.5 |      10.6 | 0.5248403 | 0.633 |     36 |    12 |  5152 | 0.007461 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.633 saved!
| 02:17:47 | 1290 |  18.9 |      10.7 | 0.5245779 | 0.633 |     41 |    12 |  5156 | 0.006713 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.633 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:18:05 | 1292 |  20.1 |      10.7 | 0.5240535 | 0.634 |      6 |    12 |  5164 | 0.000442 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.634 saved!
| 02:18:22 | 1294 |  15.7 |      10.7 | 0.5235295 | 0.634 |      4 |    12 |  5172 | 0.000620 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.634 saved!
| 02:18:32 | 1295 |  11.9 |      10.7 | 0.5232678 | 0.634 |      0 |    12 |  5176 | 0.000325 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.634 saved!
| 02:18:44 | 1296 |  11.8 |      10.7 | 0.5230062 | 0.634 |      0 |    12 |  5180 | 0.000477 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.634 saved!
| 02:18:59 | 1297 |  17.1 |      10.7 | 0.5227446 | 0.635 |      5 |    12 |  5184 | 0.000476 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.635 saved!
| 02:19:14 | 1298 |  17.0 |      10.8 | 0.5224833 | 0.636 |     10 |    12 |  5188 | 0.000287 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.636 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:19:28 | 1300 |   7.6 |      10.8 | 0.5219609 | 0.636 |      0 |    12 |  5196 | 0.000735 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1300.keras
✅ Model successfully saved to models/pong_ep1300.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1300
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.636 saved!
| 02:19:46 | 1302 |  15.7 |      10.9 | 0.5214391 | 0.636 |      0 |    12 |  5204 | 0.000449 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.636 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:20:01 | 1303 |  15.0 |      11.0 | 0.5211784 | 0.637 |      4 |    12 |  5208 | 0.000674 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.637 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:20:17 | 1304 |  17.0 |      11.1 | 0.5209178 | 0.637 |      9 |    12 |  5212 | 0.001269 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.637 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:20:33 | 1306 |  17.2 |      11.1 | 0.5203970 | 0.638 |      5 |    12 |  5220 | 0.004821 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.638 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:20:48 | 1307 |  17.2 |      11.2 | 0.5201368 | 0.638 |      0 |    12 |  5224 | 0.001205 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.638 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.639 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:21:09 | 1311 |  12.2 |      11.2 | 0.5190973 | 0.639 |      0 |    12 |  5240 | 0.000319 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.639 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.639 saved!
| 02:21:21 | 1313 |   5.3 |      11.2 | 0.5185783 | 0.639 |      0 |    12 |  5248 | 0.007570 |   50000 |
| 02:21:34 | 1314 |  20.5 |      11.3 | 0.5183190 | 0.640 |      6 |    12 |  5252 | 0.000443 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.640 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.640 saved!
| 02:21:53 | 1316 |  18.8 |      11.4 | 0.5178009 | 0.640 |     13 |    12 |  5260 | 0.000567 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745634113.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745634113.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.640 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:22:09 | 1317 |  16.2 |      11.3 | 0.5175420 | 0.641 |     17 |    12 |  5264 | 0.000426 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.641 saved!
| 02:22:23 | 1318 |  12.7 |      11.3 | 0.5172832 | 0.641 |     20 |    12 |  5268 | 0.000806 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.641 saved!
| 02:22:38 | 1319 |  18.6 |      11.4 | 0.5170245 | 0.642 |     25 |    12 |  5272 | 0.000264 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.642 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:22:54 | 1320 |  17.1 |      11.4 | 0.5167660 | 0.643 |     30 |    12 |  5276 | 0.000587 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.643 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:23:07 | 1321 |  17.5 |      11.6 | 0.5165076 | 0.643 |     35 |    12 |  5280 | 0.000289 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.643 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:23:20 | 1322 |  15.7 |      11.6 | 0.5162494 | 0.644 |     39 |    12 |  5284 | 0.005994 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.644 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:23:35 | 1325 |   7.2 |      11.3 | 0.5154754 | 0.643 |      0 |    12 |  5296 | 0.000494 |   50000 |
| 02:23:49 | 1326 |  16.8 |      11.3 | 0.5152177 | 0.644 |      5 |    12 |  5300 | 0.001150 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.644 saved!
| 02:24:08 | 1330 |  15.1 |      10.9 | 0.5141880 | 0.644 |      4 |    12 |  5316 | 0.000349 |   50000 |
| 02:24:26 | 1333 |  17.1 |      10.5 | 0.5134171 | 0.644 |      5 |    12 |  5328 | 0.000846 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.644 saved!
| 02:24:41 | 1334 |  16.4 |      10.5 | 0.5131604 | 0.645 |     10 |    12 |  5332 | 0.006170 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.645 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.645 saved!
| 02:24:59 | 1337 |  12.1 |      10.5 | 0.5123910 | 0.645 |      3 |    12 |  5344 | 0.009391 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.645 saved!
| 02:25:13 | 1338 |  18.0 |      10.6 | 0.5121349 | 0.646 |      8 |    12 |  5348 | 0.004002 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.646 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.646 saved!
| 02:25:29 | 1340 |  15.7 |      10.6 | 0.5116228 | 0.647 |     13 |    12 |  5356 | 0.003950 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.647 saved!
| 02:25:43 | 1341 |  16.7 |      10.7 | 0.5113670 | 0.647 |     17 |    12 |  5360 | 0.004808 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.647 saved!
| 02:25:56 | 1342 |  15.1 |      10.7 | 0.5111114 | 0.647 |      0 |    12 |  5364 | 0.007229 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.647 saved!
| 02:26:13 | 1343 |  20.6 |      10.8 | 0.5108558 | 0.648 |      6 |    12 |  5368 | 0.000914 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.648 saved!
| 02:26:28 | 1344 |  17.6 |      10.9 | 0.5106004 | 0.649 |      0 |    12 |  5372 | 0.000248 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.649 saved!
| 02:26:40 | 1345 |  11.5 |      10.8 | 0.5103451 | 0.649 |      3 |    12 |  5376 | 0.000459 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.649 saved!
| 02:26:55 | 1346 |  15.1 |      10.9 | 0.5100899 | 0.649 |      7 |    12 |  5380 | 0.005790 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745634415.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745634415.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.649 saved!
| 02:27:07 | 1347 |  12.1 |      11.0 | 0.5098348 | 0.650 |      0 |    12 |  5384 | 0.006214 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.650 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.650 saved!
| 02:27:21 | 1350 |   6.4 |      10.9 | 0.5090705 | 0.650 |      1 |    12 |  5396 | 0.001492 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1350.keras
✅ Model successfully saved to models/pong_ep1350.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1350
| 02:27:33 | 1351 |  14.1 |      10.8 | 0.5088159 | 0.650 |      0 |    12 |  5400 | 0.000743 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.650 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.650 saved!
| 02:27:54 | 1354 |  17.9 |      10.9 | 0.5080531 | 0.650 |      5 |    12 |  5412 | 0.000267 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.650 saved!
| 02:28:10 | 1355 |  17.6 |      10.9 | 0.5077991 | 0.651 |     10 |    12 |  5416 | 0.000469 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.651 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.651 saved!
| 02:28:26 | 1357 |   8.3 |      11.0 | 0.5072914 | 0.651 |      2 |    12 |  5424 | 0.000546 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.651 saved!
| 02:28:39 | 1358 |  15.7 |      11.0 | 0.5070378 | 0.652 |      6 |    12 |  5428 | 0.000696 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.652 saved!
| 02:28:54 | 1359 |  18.5 |      11.0 | 0.5067842 | 0.652 |     11 |    12 |  5432 | 0.000740 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.652 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.652 saved!
| 02:29:11 | 1361 |   7.7 |      11.1 | 0.5062776 | 0.652 |      0 |    12 |  5440 | 0.004392 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.652 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.652 saved!
| 02:29:31 | 1363 |  13.1 |      10.9 | 0.5057714 | 0.653 |      3 |    12 |  5448 | 0.004610 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.653 saved!
| 02:29:42 | 1364 |  14.9 |      11.0 | 0.5055185 | 0.653 |      7 |    12 |  5452 | 0.000903 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.653 saved!
| 02:29:54 | 1365 |  14.4 |      11.1 | 0.5052658 | 0.653 |      0 |    12 |  5456 | 0.000332 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.653 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.654 saved!
| 02:30:14 | 1367 |  11.3 |      11.1 | 0.5047606 | 0.654 |      0 |    12 |  5464 | 0.003825 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.654 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.654 saved!
| 02:30:27 | 1369 |   5.5 |      11.0 | 0.5042560 | 0.654 |      0 |    12 |  5472 | 0.000210 |   50000 |
| 02:30:47 | 1371 |  18.8 |      11.0 | 0.5037519 | 0.654 |      5 |    12 |  5480 | 0.000232 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.654 saved!
| 02:30:58 | 1372 |  15.6 |      11.0 | 0.5035000 | 0.655 |      9 |    12 |  5484 | 0.011957 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.655 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.655 saved!
| 02:31:08 | 1374 |   5.8 |      11.0 | 0.5029966 | 0.655 |     11 |    12 |  5492 | 0.000847 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.655 saved!
| 02:31:18 | 1375 |  11.5 |      10.9 | 0.5027451 | 0.655 |     14 |    12 |  5496 | 0.005883 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.655 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.656 saved!
| 02:31:32 | 1377 |   5.2 |      11.0 | 0.5022425 | 0.656 |     18 |    12 |  5504 | 0.000696 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.656 saved!
| 02:31:45 | 1378 |  14.9 |      11.0 | 0.5019914 | 0.656 |      0 |    12 |  5508 | 0.000876 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.656 saved!
| 02:31:59 | 1379 |  18.2 |      11.0 | 0.5017404 | 0.657 |      5 |    12 |  5512 | 0.000605 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745634719.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745634719.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.657 saved!
| 02:32:14 | 1380 |  17.0 |      11.2 | 0.5014895 | 0.657 |     10 |    12 |  5516 | 0.012961 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.657 saved!
| 02:32:24 | 1381 |  13.9 |      11.2 | 0.5012388 | 0.658 |     13 |    12 |  5520 | 0.001287 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.658 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.658 saved!
| 02:32:50 | 1383 |  18.3 |      11.3 | 0.5007377 | 0.659 |     21 |    12 |  5528 | 0.000960 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.659 saved!
| 02:33:06 | 1384 |  16.1 |      11.4 | 0.5004873 | 0.659 |     25 |    12 |  5532 | 0.000469 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.659 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.659 saved!
| 02:33:25 | 1386 |  19.7 |      11.3 | 0.4999869 | 0.660 |     31 |    12 |  5540 | 0.000519 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.660 saved!
| 02:33:35 | 1387 |  13.8 |      11.2 | 0.4997369 | 0.660 |     34 |    12 |  5544 | 0.000376 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.660 saved!
| 02:33:45 | 1388 |  11.9 |      11.2 | 0.4994871 | 0.661 |     37 |    12 |  5548 | 0.000476 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.661 saved!
| 02:34:01 | 1389 |  16.9 |      11.2 | 0.4992373 | 0.661 |     42 |    12 |  5552 | 0.000440 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.661 saved!
| 02:34:15 | 1390 |  17.8 |      11.2 | 0.4989877 | 0.662 |     47 |    12 |  5556 | 0.006826 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.662 saved!
| 02:34:35 | 1392 |  19.5 |      11.2 | 0.4984888 | 0.662 |     53 |    12 |  5564 | 0.005901 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.662 saved!
| 02:34:52 | 1393 |  17.9 |      11.4 | 0.4982396 | 0.663 |     58 |    12 |  5568 | 0.000445 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.663 saved!
| 02:35:07 | 1394 |  20.7 |      11.4 | 0.4979905 | 0.664 |     64 |    12 |  5572 | 0.000497 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.664 saved!
| 02:35:24 | 1395 |  18.2 |      11.5 | 0.4977415 | 0.664 |     69 |    12 |  5576 | 0.005264 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.664 saved!
| 02:35:40 | 1396 |  16.2 |      11.5 | 0.4974926 | 0.665 |     74 |    12 |  5580 | 0.000563 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.665 saved!
| 02:35:55 | 1397 |  17.7 |      11.5 | 0.4972439 | 0.665 |     79 |    12 |  5584 | 0.004663 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.665 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.666 saved!
| 02:36:19 | 1399 |  18.3 |      11.6 | 0.4967468 | 0.666 |     86 |    12 |  5592 | 0.000332 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.666 saved!
| 02:36:36 | 1400 |  16.3 |      11.7 | 0.4964984 | 0.667 |     91 |    12 |  5596 | 0.000423 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1400.keras
✅ Model successfully saved to models/pong_ep1400.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1400
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.667 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_milestone_1400.keras
🏆 Milestone save at episode 1400
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:36:49 | 1402 |   1.8 |      11.6 | 0.4960020 | 0.666 |      0 |    12 |  5604 | 0.000706 |   50000 |
| 02:37:10 | 1404 |  12.3 |      11.5 | 0.4955061 | 0.667 |      0 |    12 |  5612 | 0.000430 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745635030.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745635030.keras
| 02:37:28 | 1406 |  20.5 |      11.5 | 0.4950107 | 0.667 |      6 |    12 |  5620 | 0.000220 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.667 saved!
| 02:37:49 | 1408 |  14.9 |      11.5 | 0.4945159 | 0.667 |      0 |    12 |  5628 | 0.000534 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.667 saved!
| 02:38:01 | 1409 |  15.1 |      11.6 | 0.4942686 | 0.668 |      4 |    12 |  5632 | 0.000617 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.668 saved!
| 02:38:14 | 1410 |  16.4 |      11.7 | 0.4940215 | 0.668 |      8 |    12 |  5636 | 0.000472 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.668 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.668 saved!
| 02:38:25 | 1412 |   5.1 |      11.7 | 0.4935276 | 0.669 |     11 |    12 |  5644 | 0.000226 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.669 saved!
| 02:38:41 | 1413 |  17.3 |      11.8 | 0.4932808 | 0.669 |     16 |    12 |  5648 | 0.000285 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.669 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:38:56 | 1415 |  11.0 |      11.7 | 0.4927876 | 0.669 |      0 |    12 |  5656 | 0.000298 |   50000 |
| 02:39:12 | 1416 |  16.0 |      11.6 | 0.4925413 | 0.669 |      4 |    12 |  5660 | 0.000275 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.669 saved!
| 02:39:28 | 1417 |  19.3 |      11.7 | 0.4922950 | 0.670 |      9 |    12 |  5664 | 0.000588 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.670 saved!
| 02:39:40 | 1418 |  13.9 |      11.7 | 0.4920488 | 0.670 |     12 |    12 |  5668 | 0.000611 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.670 saved!
| 02:39:55 | 1419 |  16.3 |      11.7 | 0.4918028 | 0.671 |     16 |    12 |  5672 | 0.000355 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.671 saved!
| 02:40:12 | 1421 |  17.1 |      11.5 | 0.4913111 | 0.671 |      5 |    12 |  5680 | 0.000227 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.671 saved!
| 02:40:27 | 1422 |  17.9 |      11.5 | 0.4910655 | 0.672 |     10 |    12 |  5684 | 0.002404 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.672 saved!
| 02:40:50 | 1424 |  22.1 |      11.7 | 0.4905745 | 0.672 |      6 |    12 |  5692 | 0.000794 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.672 saved!
| 02:41:06 | 1425 |  13.5 |      11.8 | 0.4903292 | 0.673 |     10 |    12 |  5696 | 0.005316 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.673 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:41:24 | 1426 |  17.1 |      11.8 | 0.4900841 | 0.673 |     15 |    12 |  5700 | 0.001079 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.673 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:41:37 | 1427 |  12.9 |      11.9 | 0.4898390 | 0.673 |      0 |    12 |  5704 | 0.001142 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.673 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.673 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:41:53 | 1429 |  11.8 |      12.1 | 0.4893493 | 0.673 |      0 |    12 |  5712 | 0.000359 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.673 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.674 saved!
| 02:42:12 | 1431 |  15.2 |      12.2 | 0.4888601 | 0.674 |      6 |    12 |  5720 | 0.000391 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745635332.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745635332.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.674 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:42:35 | 1433 |  14.2 |      12.2 | 0.4883714 | 0.674 |      4 |    12 |  5728 | 0.000634 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.674 saved!
| 02:42:49 | 1436 |   4.2 |      12.1 | 0.4876392 | 0.674 |      1 |    12 |  5740 | 0.000462 |   50000 |
| 02:43:04 | 1437 |  14.8 |      12.1 | 0.4873953 | 0.675 |      0 |    12 |  5744 | 0.000241 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.675 saved!
| 02:43:19 | 1438 |  14.1 |      12.0 | 0.4871516 | 0.675 |      0 |    12 |  5748 | 0.005705 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.675 saved!
| 02:43:33 | 1439 |  19.0 |      12.2 | 0.4869081 | 0.675 |      5 |    12 |  5752 | 0.000346 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.675 saved!
| 02:43:51 | 1440 |  18.1 |      12.2 | 0.4866646 | 0.676 |     10 |    12 |  5756 | 0.000445 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.676 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.676 saved!
| 02:44:10 | 1442 |  19.3 |      12.1 | 0.4861781 | 0.676 |     16 |    12 |  5764 | 0.000257 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.676 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.677 saved!
| 02:44:28 | 1444 |   8.0 |      12.0 | 0.4856920 | 0.677 |      0 |    12 |  5772 | 0.000303 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.677 saved!
| 02:44:47 | 1446 |  18.7 |      11.9 | 0.4852064 | 0.677 |      7 |    12 |  5780 | 0.000176 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.677 saved!
| 02:45:03 | 1447 |  20.0 |      12.0 | 0.4849638 | 0.678 |     13 |    12 |  5784 | 0.006480 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.678 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.678 saved!
| 02:45:15 | 1449 |   1.4 |      12.0 | 0.4844790 | 0.678 |      0 |    12 |  5792 | 0.001270 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1450.keras
✅ Model successfully saved to models/pong_ep1450.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1450
| 02:45:33 | 1451 |   8.5 |      12.0 | 0.4839946 | 0.678 |      4 |    12 |  5800 | 0.000719 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.678 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.679 saved!
| 02:45:53 | 1453 |  17.4 |      12.2 | 0.4835108 | 0.679 |     10 |    12 |  5808 | 0.000345 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.679 saved!
| 02:46:09 | 1454 |  15.2 |      12.1 | 0.4832690 | 0.679 |     14 |    12 |  5812 | 0.000725 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.679 saved!
| 02:46:25 | 1455 |  17.1 |      12.1 | 0.4830274 | 0.680 |     19 |    12 |  5816 | 0.000543 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.680 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.680 saved!
| 02:46:36 | 1458 |   0.7 |      11.9 | 0.4823032 | 0.680 |      0 |    12 |  5828 | 0.000966 |   50000 |
| 02:46:49 | 1459 |  14.2 |      11.9 | 0.4820621 | 0.680 |      0 |    12 |  5832 | 0.005721 |   50000 |
| 02:47:05 | 1460 |  15.2 |      11.9 | 0.4818210 | 0.680 |      4 |    12 |  5836 | 0.004303 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.680 saved!
| 02:47:23 | 1462 |  15.1 |      12.0 | 0.4813393 | 0.680 |      0 |    12 |  5844 | 0.000374 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745635643.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745635643.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.680 saved!
| 02:47:34 | 1463 |  11.9 |      11.9 | 0.4810987 | 0.681 |      0 |    12 |  5848 | 0.000735 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.681 saved!
| 02:47:48 | 1464 |  14.9 |      11.9 | 0.4808581 | 0.681 |      4 |    12 |  5852 | 0.005611 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.681 saved!
| 02:48:04 | 1465 |  15.1 |      11.9 | 0.4806177 | 0.681 |      8 |    12 |  5856 | 0.000524 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.681 saved!
| 02:48:21 | 1466 |  18.1 |      12.0 | 0.4803774 | 0.682 |     13 |    12 |  5860 | 0.001014 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.682 saved!
| 02:48:36 | 1467 |  16.4 |      12.1 | 0.4801372 | 0.682 |     18 |    12 |  5864 | 0.000475 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.682 saved!
| 02:48:52 | 1468 |  16.6 |      12.2 | 0.4798971 | 0.683 |     23 |    12 |  5868 | 0.000363 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.683 saved!
| 02:49:09 | 1470 |  16.2 |      12.2 | 0.4794173 | 0.683 |      5 |    12 |  5876 | 0.000620 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.683 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:49:31 | 1472 |  11.5 |      12.1 | 0.4789380 | 0.683 |      0 |    12 |  5884 | 0.000259 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.683 saved!
| 02:49:47 | 1473 |  20.6 |      12.3 | 0.4786986 | 0.684 |      5 |    12 |  5888 | 0.000240 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.684 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 02:50:00 | 1474 |  14.2 |      12.3 | 0.4784592 | 0.684 |      0 |    12 |  5892 | 0.000469 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.684 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.684 saved!
| 02:50:26 | 1476 |  17.0 |      12.4 | 0.4779809 | 0.685 |      7 |    12 |  5900 | 0.007362 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.685 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.685 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.685 saved!
| 02:50:42 | 1479 |   9.8 |      12.2 | 0.4772643 | 0.685 |     12 |    12 |  5912 | 0.000478 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.685 saved!
| 02:51:05 | 1481 |  20.1 |      12.2 | 0.4767871 | 0.686 |      6 |    12 |  5920 | 0.000953 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.686 saved!
| 02:51:17 | 1482 |  17.0 |      12.2 | 0.4765487 | 0.686 |     10 |    12 |  5924 | 0.000701 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.686 saved!
| 02:51:35 | 1483 |  17.0 |      12.2 | 0.4763104 | 0.686 |     15 |    12 |  5928 | 0.000747 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.686 saved!
| 02:51:55 | 1486 |  13.1 |      12.0 | 0.4755963 | 0.686 |      3 |    12 |  5940 | 0.000322 |   50000 |
| 02:52:11 | 1487 |  10.7 |      12.0 | 0.4753585 | 0.687 |      0 |    12 |  5944 | 0.000402 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.687 saved!
| 02:52:22 | 1488 |   8.4 |      11.9 | 0.4751209 | 0.687 |      0 |    12 |  5948 | 0.000309 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745635949.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745635949.keras
| 02:52:45 | 1490 |  16.3 |      11.8 | 0.4746459 | 0.687 |      5 |    12 |  5956 | 0.001310 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.687 saved!
| 02:52:57 | 1491 |  11.7 |      11.9 | 0.4744085 | 0.687 |      0 |    12 |  5960 | 0.000417 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.687 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.687 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.687 saved!
| 02:53:21 | 1494 |  16.5 |      11.6 | 0.4736973 | 0.688 |      0 |    12 |  5972 | 0.006247 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.688 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.688 saved!
| 02:53:34 | 1496 |   3.9 |      11.4 | 0.4732237 | 0.688 |      0 |    12 |  5980 | 0.000641 |   50000 |
| 02:53:45 | 1498 |   4.0 |      11.2 | 0.4727506 | 0.687 |      0 |    12 |  5988 | 0.000694 |   50000 |
| 02:54:04 | 1500 |  16.5 |      11.1 | 0.4722780 | 0.688 |      5 |    12 |  5996 | 0.000787 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1500.keras
✅ Model successfully saved to models/pong_ep1500.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1500
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.688 saved!
| 02:54:20 | 1501 |  19.4 |      11.2 | 0.4720418 | 0.688 |     11 |    12 |  6000 | 0.000489 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.688 saved!
| 02:54:45 | 1503 |  17.8 |      11.3 | 0.4715699 | 0.689 |      5 |    12 |  6008 | 0.000654 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.689 saved!
| 02:55:04 | 1505 |  16.8 |      11.4 | 0.4710984 | 0.689 |      5 |    12 |  6016 | 0.000524 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.689 saved!
| 02:55:20 | 1506 |  20.3 |      11.4 | 0.4708629 | 0.690 |     11 |    12 |  6020 | 0.000517 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.690 saved!
| 02:55:38 | 1507 |  19.8 |      11.5 | 0.4706275 | 0.690 |     17 |    12 |  6024 | 0.000294 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.690 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.690 saved!
| 02:55:59 | 1509 |  11.9 |      11.5 | 0.4701570 | 0.690 |      0 |    12 |  6032 | 0.000482 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.690 saved!
| 02:56:10 | 1511 |   4.7 |      11.3 | 0.4696869 | 0.691 |      1 |    12 |  6040 | 0.011001 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.691 saved!
| 02:56:27 | 1512 |  16.6 |      11.4 | 0.4694521 | 0.691 |      6 |    12 |  6044 | 0.000482 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.691 saved!
| 02:56:42 | 1513 |  14.6 |      11.4 | 0.4692173 | 0.691 |     10 |    12 |  6048 | 0.000799 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.691 saved!
| 02:57:00 | 1516 |   7.7 |      11.3 | 0.4685139 | 0.691 |      0 |    12 |  6060 | 0.000710 |   50000 |
| 02:57:10 | 1517 |  10.8 |      11.2 | 0.4682796 | 0.691 |      0 |    12 |  6064 | 0.000377 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.691 saved!
| 02:57:20 | 1518 |  12.2 |      11.2 | 0.4680455 | 0.692 |      3 |    12 |  6068 | 0.000184 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.692 saved!
| 02:57:31 | 1519 |  12.0 |      11.2 | 0.4678115 | 0.692 |      6 |    12 |  6072 | 0.000388 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745636251.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745636251.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.692 saved!
| 02:57:49 | 1520 |  20.3 |      11.4 | 0.4675775 | 0.692 |     12 |    12 |  6076 | 0.000212 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.692 saved!
| 02:58:00 | 1521 |  12.6 |      11.3 | 0.4673438 | 0.693 |     15 |    12 |  6080 | 0.000531 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.693 saved!
| 02:58:19 | 1523 |  18.5 |      11.3 | 0.4668765 | 0.693 |      5 |    12 |  6088 | 0.000360 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.693 saved!
| 02:58:36 | 1524 |  17.7 |      11.2 | 0.4666431 | 0.693 |     10 |    12 |  6092 | 0.000258 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.693 saved!
| 02:58:50 | 1525 |  15.0 |      11.3 | 0.4664098 | 0.694 |      0 |    12 |  6096 | 0.000154 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.694 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.694 saved!
| 02:59:12 | 1527 |  19.2 |      11.2 | 0.4659435 | 0.694 |      8 |    12 |  6104 | 0.000136 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.694 saved!
| 02:59:32 | 1530 |  17.6 |      11.2 | 0.4652449 | 0.694 |      5 |    12 |  6116 | 0.000368 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.694 saved!
| 02:59:48 | 1531 |  19.4 |      11.2 | 0.4650123 | 0.695 |     10 |    12 |  6120 | 0.000341 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.695 saved!
| 03:00:03 | 1532 |  17.7 |      11.3 | 0.4647798 | 0.695 |     15 |    12 |  6124 | 0.000368 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.695 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.695 saved!
| 03:00:19 | 1534 |  14.6 |      11.4 | 0.4643151 | 0.696 |     19 |    12 |  6132 | 0.000315 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.696 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.696 saved!
| 03:00:43 | 1536 |  21.4 |      11.6 | 0.4638509 | 0.696 |     28 |    12 |  6140 | 0.000314 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.696 saved!
| 03:00:58 | 1537 |  19.2 |      11.6 | 0.4636190 | 0.697 |     33 |    12 |  6144 | 0.000248 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.697 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.697 saved!
| 03:01:10 | 1539 |   8.4 |      11.4 | 0.4631555 | 0.697 |     36 |    12 |  6152 | 0.007144 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.697 saved!
| 03:01:26 | 1540 |  19.7 |      11.5 | 0.4629239 | 0.698 |     41 |    12 |  6156 | 0.015887 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.698 saved!
| 03:01:46 | 1542 |  11.6 |      11.4 | 0.4624611 | 0.698 |      0 |    12 |  6164 | 0.006835 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.698 saved!
| 03:01:56 | 1543 |  13.4 |      11.4 | 0.4622299 | 0.698 |      3 |    12 |  6168 | 0.001296 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.698 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.698 saved!
| 03:02:13 | 1545 |  12.7 |      11.5 | 0.4617678 | 0.698 |      8 |    12 |  6176 | 0.000515 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.698 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.698 saved!
| 03:02:33 | 1547 |  17.3 |      11.3 | 0.4613061 | 0.699 |     14 |    12 |  6184 | 0.000619 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745636553.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745636553.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.699 saved!
| 03:02:48 | 1548 |  19.9 |      11.4 | 0.4610755 | 0.699 |     20 |    12 |  6188 | 0.000359 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.699 saved!
| 03:03:04 | 1549 |  18.1 |      11.6 | 0.4608449 | 0.700 |     25 |    12 |  6192 | 0.007523 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.700 saved!
| 03:03:19 | 1550 |  18.9 |      11.7 | 0.4606145 | 0.700 |     31 |    12 |  6196 | 0.013045 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1550.keras
✅ Model successfully saved to models/pong_ep1550.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1550
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.700 saved!
| 03:03:33 | 1551 |  18.9 |      11.8 | 0.4603842 | 0.701 |     37 |    12 |  6200 | 0.001356 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.701 saved!
| 03:03:50 | 1552 |  20.3 |      12.0 | 0.4601540 | 0.701 |     43 |    12 |  6204 | 0.001105 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.701 saved!
| 03:04:08 | 1553 |  19.0 |      12.0 | 0.4599239 | 0.702 |     48 |    12 |  6208 | 0.006652 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.702 saved!
| 03:04:23 | 1554 |  16.7 |      12.0 | 0.4596940 | 0.702 |     53 |    12 |  6212 | 0.000460 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.702 saved!
| 03:04:41 | 1556 |   9.2 |      11.9 | 0.4592344 | 0.702 |      0 |    12 |  6220 | 0.000217 |   50000 |
| 03:04:56 | 1557 |  19.0 |      12.1 | 0.4590048 | 0.703 |      5 |    12 |  6224 | 0.000290 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.703 saved!
| 03:05:12 | 1558 |  19.6 |      12.3 | 0.4587753 | 0.703 |     11 |    12 |  6228 | 0.000366 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.703 saved!
| 03:05:36 | 1561 |  18.5 |      12.2 | 0.4580874 | 0.703 |      5 |    12 |  6240 | 0.007935 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.703 saved!
| 03:05:48 | 1562 |  12.2 |      12.2 | 0.4578584 | 0.703 |      8 |    12 |  6244 | 0.000316 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.703 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.703 saved!
| 03:06:03 | 1564 |  11.2 |      12.1 | 0.4574007 | 0.704 |      0 |    12 |  6252 | 0.000407 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:06:15 | 1566 |   9.5 |      11.9 | 0.4569434 | 0.703 |      2 |    12 |  6260 | 0.000387 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:06:29 | 1568 |   6.2 |      11.7 | 0.4564865 | 0.704 |      5 |    12 |  6268 | 0.000441 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:06:41 | 1570 |   4.4 |      11.7 | 0.4560302 | 0.704 |      1 |    12 |  6276 | 0.000670 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:06:53 | 1571 |  11.1 |      11.7 | 0.4558022 | 0.704 |      0 |    12 |  6280 | 0.000268 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:07:09 | 1573 |  15.2 |      11.5 | 0.4553465 | 0.704 |      0 |    12 |  6288 | 0.000246 |   50000 |
| 03:07:24 | 1574 |  17.6 |      11.5 | 0.4551188 | 0.704 |      5 |    12 |  6292 | 0.000447 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:07:40 | 1575 |  15.6 |      11.6 | 0.4548912 | 0.704 |      0 |    12 |  6296 | 0.000177 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745636860.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745636860.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.704 saved!
| 03:07:56 | 1576 |  16.4 |      11.6 | 0.4546638 | 0.705 |      5 |    12 |  6300 | 0.000285 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.705 saved!
| 03:08:13 | 1577 |  16.9 |      11.7 | 0.4544365 | 0.705 |     10 |    12 |  6304 | 0.000123 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.705 saved!
| 03:08:26 | 1579 |   8.1 |      11.6 | 0.4539821 | 0.705 |      0 |    12 |  6312 | 0.000149 |   50000 |
| 03:08:40 | 1580 |  18.2 |      11.7 | 0.4537551 | 0.705 |      5 |    12 |  6316 | 0.000374 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.705 saved!
| 03:08:56 | 1581 |  18.5 |      11.7 | 0.4535283 | 0.706 |     10 |    12 |  6320 | 0.007480 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.706 saved!
| 03:09:11 | 1582 |  14.8 |      11.7 | 0.4533015 | 0.706 |     14 |    12 |  6324 | 0.000255 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.706 saved!
| 03:09:28 | 1583 |  19.0 |      11.7 | 0.4530748 | 0.706 |     19 |    12 |  6328 | 0.005829 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.706 saved!
| 03:09:39 | 1584 |   8.7 |      11.8 | 0.4528483 | 0.706 |      0 |    12 |  6332 | 0.000229 |   50000 |
| 03:09:53 | 1586 |   5.3 |      11.7 | 0.4523956 | 0.707 |      1 |    12 |  6340 | 0.000494 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.707 saved!
| 03:10:11 | 1588 |  16.9 |      11.7 | 0.4519433 | 0.707 |      4 |    12 |  6348 | 0.000516 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.707 saved!
| 03:10:21 | 1589 |   9.1 |      11.7 | 0.4517173 | 0.707 |      0 |    12 |  6352 | 0.007174 |   50000 |
| 03:10:32 | 1592 |   8.2 |      11.5 | 0.4510401 | 0.707 |      2 |    12 |  6364 | 0.000589 |   50000 |
| 03:10:43 | 1593 |  13.3 |      11.6 | 0.4508146 | 0.707 |      5 |    12 |  6368 | 0.000218 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.707 saved!
| 03:10:59 | 1594 |  15.8 |      11.6 | 0.4505892 | 0.707 |      9 |    12 |  6372 | 0.000178 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.707 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.707 saved!
| 03:11:17 | 1596 |  13.6 |      11.7 | 0.4501387 | 0.708 |     14 |    12 |  6380 | 0.000315 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.708 saved!
| 03:11:28 | 1597 |   8.1 |      11.7 | 0.4499136 | 0.707 |      0 |    12 |  6384 | 0.000207 |   50000 |
| 03:11:44 | 1598 |  16.1 |      11.8 | 0.4496887 | 0.708 |      5 |    12 |  6388 | 0.006343 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.708 saved!
| 03:11:56 | 1599 |  12.2 |      11.9 | 0.4494638 | 0.708 |      0 |    12 |  6392 | 0.000322 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.708 saved!
Attempting to save model to: /kaggle/working/models/pong_ep1600.keras
✅ Model successfully saved to models/pong_ep1600.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1600
✅ Model successfully force-saved to models/pong_milestone_1600.keras
🏆 Milestone save at episode 1600
| 03:12:07 | 1601 |   2.0 |      11.7 | 0.4490145 | 0.708 |      0 |    12 |  6400 | 0.000810 |   50000 |
| 03:12:23 | 1603 |  15.2 |      11.6 | 0.4485656 | 0.708 |      4 |    12 |  6408 | 0.005416 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.708 saved!
| 03:12:41 | 1605 |  18.8 |      11.6 | 0.4481171 | 0.708 |      5 |    12 |  6416 | 0.004938 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745637161.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745637161.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.708 saved!
| 03:13:03 | 1607 |  13.9 |      11.4 | 0.4476691 | 0.708 |      0 |    12 |  6424 | 0.006747 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.708 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.709 saved!
| 03:13:29 | 1609 |  18.9 |      11.5 | 0.4472215 | 0.709 |      8 |    12 |  6432 | 0.000339 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.709 saved!
| 03:13:46 | 1612 |   9.2 |      11.4 | 0.4465510 | 0.709 |      2 |    12 |  6444 | 0.000798 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.709 saved!
| 03:14:02 | 1613 |  17.9 |      11.4 | 0.4463278 | 0.709 |      7 |    12 |  6448 | 0.000375 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.709 saved!
| 03:14:15 | 1614 |  14.0 |      11.6 | 0.4461046 | 0.710 |      0 |    12 |  6452 | 0.000465 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.710 saved!
| 03:14:26 | 1616 |  10.3 |      11.5 | 0.4456586 | 0.709 |      2 |    12 |  6460 | 0.000361 |   50000 |
| 03:14:42 | 1617 |  20.2 |      11.6 | 0.4454358 | 0.710 |      8 |    12 |  6464 | 0.000237 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.710 saved!
| 03:14:55 | 1618 |  16.5 |      11.6 | 0.4452131 | 0.710 |     12 |    12 |  6468 | 0.009675 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.710 saved!
| 03:15:12 | 1620 |   7.1 |      11.5 | 0.4447680 | 0.710 |      0 |    12 |  6476 | 0.007872 |   50000 |
| 03:15:33 | 1622 |  14.3 |      11.5 | 0.4443233 | 0.710 |      0 |    12 |  6484 | 0.001152 |   50000 |
| 03:15:53 | 1625 |  12.7 |      11.2 | 0.4436572 | 0.710 |      4 |    12 |  6496 | 0.000950 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.710 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.710 saved!
| 03:16:10 | 1627 |   9.9 |      11.1 | 0.4432136 | 0.711 |      8 |    12 |  6504 | 0.000557 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.711 saved!
| 03:16:27 | 1628 |  20.5 |      11.3 | 0.4429920 | 0.711 |     13 |    12 |  6508 | 0.000429 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.711 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.711 saved!
| 03:16:44 | 1630 |  11.9 |      11.3 | 0.4425491 | 0.711 |     18 |    12 |  6516 | 0.000517 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.711 saved!
| 03:16:57 | 1631 |  16.7 |      11.3 | 0.4423278 | 0.712 |     22 |    12 |  6520 | 0.000798 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.712 saved!
| 03:17:13 | 1632 |  19.6 |      11.3 | 0.4421067 | 0.712 |     27 |    12 |  6524 | 0.000370 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.712 saved!
| 03:17:23 | 1633 |   8.9 |      11.4 | 0.4418856 | 0.712 |      0 |    12 |  6528 | 0.000541 |   50000 |
| 03:17:50 | 1635 |  16.8 |      11.3 | 0.4414439 | 0.712 |      5 |    12 |  6536 | 0.000638 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745637470.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745637470.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.712 saved!
| 03:18:16 | 1637 |  14.1 |      11.1 | 0.4410025 | 0.713 |      4 |    12 |  6544 | 0.000501 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.713 saved!
| 03:18:33 | 1638 |  17.9 |      11.3 | 0.4407820 | 0.713 |      9 |    12 |  6548 | 0.000473 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.713 saved!
| 03:18:50 | 1639 |  16.0 |      11.3 | 0.4405616 | 0.713 |     13 |    12 |  6552 | 0.000518 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.713 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.714 saved!
| 03:19:09 | 1641 |  11.9 |      11.3 | 0.4401212 | 0.714 |     19 |    12 |  6560 | 0.000412 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.714 saved!
| 03:19:27 | 1643 |  18.0 |      11.3 | 0.4396812 | 0.714 |     24 |    12 |  6568 | 0.006551 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.714 saved!
| 03:19:43 | 1645 |  12.9 |      11.2 | 0.4392416 | 0.714 |      3 |    12 |  6576 | 0.000323 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.714 saved!
| 03:20:07 | 1647 |  21.4 |      11.3 | 0.4388025 | 0.715 |      6 |    12 |  6584 | 0.006968 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.715 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.715 saved!
| 03:20:28 | 1649 |  17.1 |      11.1 | 0.4383638 | 0.715 |     12 |    12 |  6592 | 0.000369 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.715 saved!
| 03:20:44 | 1650 |  14.0 |      11.1 | 0.4381446 | 0.715 |     16 |    12 |  6596 | 0.000582 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1650.keras
✅ Model successfully saved to models/pong_ep1650.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1650
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.715 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.716 saved!
| 03:20:58 | 1652 |   3.9 |      10.8 | 0.4377066 | 0.715 |      0 |    12 |  6604 | 0.000238 |   50000 |
| 03:21:17 | 1654 |  18.3 |      10.7 | 0.4372690 | 0.716 |      6 |    12 |  6612 | 0.000512 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.716 saved!
| 03:21:31 | 1655 |  11.4 |      10.7 | 0.4370503 | 0.716 |      0 |    12 |  6616 | 0.000664 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.716 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.716 saved!
| 03:21:55 | 1658 |  15.5 |      10.4 | 0.4363951 | 0.716 |      0 |    12 |  6628 | 0.005039 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.716 saved!
| 03:22:06 | 1659 |  11.8 |      10.5 | 0.4361769 | 0.716 |      3 |    12 |  6632 | 0.007373 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.716 saved!
| 03:22:22 | 1661 |  14.9 |      10.5 | 0.4357408 | 0.717 |      7 |    12 |  6640 | 0.006169 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.717 saved!
| 03:22:39 | 1662 |  15.2 |      10.5 | 0.4355229 | 0.717 |      0 |    12 |  6644 | 0.000403 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.717 saved!
| 03:22:54 | 1663 |  20.4 |      10.7 | 0.4353052 | 0.717 |      6 |    12 |  6648 | 0.000509 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745637774.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745637774.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.717 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.717 saved!
| 03:23:20 | 1665 |  17.0 |      10.8 | 0.4348700 | 0.718 |     14 |    12 |  6656 | 0.000479 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.718 saved!
| 03:23:37 | 1666 |  16.0 |      10.9 | 0.4346525 | 0.718 |     18 |    12 |  6660 | 0.000369 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.718 saved!
| 03:23:54 | 1667 |  21.2 |      11.0 | 0.4344352 | 0.719 |     24 |    12 |  6664 | 0.000522 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.719 saved!
| 03:24:09 | 1668 |  13.3 |      11.1 | 0.4342180 | 0.719 |     27 |    12 |  6668 | 0.004713 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.719 saved!
| 03:24:26 | 1669 |  20.3 |      11.2 | 0.4340009 | 0.719 |     32 |    12 |  6672 | 0.000216 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.719 saved!
| 03:24:42 | 1671 |  15.3 |      11.2 | 0.4335670 | 0.719 |      4 |    12 |  6680 | 0.000464 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.719 saved!
| 03:24:54 | 1672 |  16.0 |      11.4 | 0.4333502 | 0.720 |      8 |    12 |  6684 | 0.000442 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.720 saved!
| 03:25:14 | 1674 |  19.2 |      11.3 | 0.4329170 | 0.720 |      5 |    12 |  6692 | 0.000909 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.720 saved!
| 03:25:24 | 1676 |   5.3 |      11.0 | 0.4324842 | 0.720 |      1 |    12 |  6700 | 0.000297 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.720 saved!
| 03:25:49 | 1678 |  18.7 |      11.2 | 0.4320518 | 0.720 |      9 |    12 |  6708 | 0.001054 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.720 saved!
| 03:26:05 | 1679 |  18.9 |      11.3 | 0.4318358 | 0.721 |     14 |    12 |  6712 | 0.006348 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.721 saved!
| 03:26:21 | 1680 |  18.3 |      11.3 | 0.4316198 | 0.721 |     19 |    12 |  6716 | 0.004631 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.721 saved!
| 03:26:39 | 1681 |  17.7 |      11.3 | 0.4314040 | 0.721 |      0 |    12 |  6720 | 0.006598 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.721 saved!
| 03:26:55 | 1682 |  15.3 |      11.3 | 0.4311883 | 0.721 |      4 |    12 |  6724 | 0.006187 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.721 saved!
| 03:27:11 | 1683 |  16.1 |      11.2 | 0.4309727 | 0.722 |      9 |    12 |  6728 | 0.001090 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.722 saved!
| 03:27:28 | 1684 |  16.7 |      11.3 | 0.4307573 | 0.722 |     14 |    12 |  6732 | 0.001028 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.722 saved!
| 03:27:47 | 1685 |  16.1 |      11.4 | 0.4305419 | 0.722 |     19 |    12 |  6736 | 0.000805 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.722 saved!
| 03:28:05 | 1686 |  17.3 |      11.5 | 0.4303266 | 0.723 |     24 |    12 |  6740 | 0.000433 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745638085.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745638085.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.723 saved!
| 03:28:20 | 1687 |  15.5 |      11.7 | 0.4301114 | 0.723 |     28 |    12 |  6744 | 0.006271 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.723 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.723 saved!
| 03:28:38 | 1689 |  15.6 |      11.6 | 0.4296814 | 0.723 |     33 |    12 |  6752 | 0.007360 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.723 saved!
| 03:28:52 | 1690 |  11.3 |      11.7 | 0.4294666 | 0.724 |      0 |    12 |  6756 | 0.000930 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
| 03:29:12 | 1692 |  15.3 |      11.8 | 0.4290372 | 0.724 |      5 |    12 |  6764 | 0.000469 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
| 03:29:25 | 1694 |   9.6 |      11.6 | 0.4286083 | 0.724 |      2 |    12 |  6772 | 0.000284 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
| 03:29:46 | 1696 |  20.0 |      11.6 | 0.4281798 | 0.724 |      9 |    12 |  6780 | 0.000345 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
| 03:30:02 | 1697 |  15.9 |      11.7 | 0.4279657 | 0.724 |      0 |    12 |  6784 | 0.000639 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.724 saved!
| 03:30:13 | 1699 |   8.4 |      11.6 | 0.4275379 | 0.725 |      3 |    12 |  6792 | 0.000241 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.725 saved!
Attempting to save model to: /kaggle/working/models/pong_ep1700.keras
✅ Model successfully saved to models/pong_ep1700.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1700
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.725 saved!
| 03:30:39 | 1701 |  20.5 |      11.8 | 0.4271104 | 0.725 |     11 |    12 |  6800 | 0.000467 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.725 saved!
| 03:30:51 | 1702 |  16.2 |      11.9 | 0.4268969 | 0.725 |     15 |    12 |  6804 | 0.000318 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.725 saved!
| 03:31:05 | 1703 |  17.2 |      11.9 | 0.4266834 | 0.726 |     20 |    12 |  6808 | 0.000353 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.726 saved!
| 03:31:19 | 1704 |  16.2 |      12.1 | 0.4264701 | 0.726 |     24 |    12 |  6812 | 0.000283 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.726 saved!
| 03:31:40 | 1706 |  18.8 |      12.0 | 0.4260437 | 0.726 |      5 |    12 |  6820 | 0.006437 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.726 saved!
| 03:31:56 | 1707 |  14.4 |      12.0 | 0.4258307 | 0.726 |      9 |    12 |  6824 | 0.001602 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.726 saved!
| 03:32:06 | 1709 |   1.7 |      11.7 | 0.4254050 | 0.726 |      0 |    12 |  6832 | 0.005505 |   50000 |
| 03:32:26 | 1711 |  17.6 |      11.9 | 0.4249797 | 0.727 |      6 |    12 |  6840 | 0.011208 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
| 03:32:39 | 1712 |  12.5 |      11.9 | 0.4247672 | 0.727 |      0 |    12 |  6844 | 0.001331 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
| 03:32:53 | 1715 |   4.3 |      11.7 | 0.4241303 | 0.726 |      0 |    12 |  6856 | 0.000224 |   50000 |
| 03:33:09 | 1716 |  19.3 |      11.8 | 0.4239183 | 0.727 |      5 |    12 |  6860 | 0.000294 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745638389.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745638389.keras
| 03:33:22 | 1717 |  12.2 |      11.7 | 0.4237063 | 0.727 |      0 |    12 |  6864 | 0.000279 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
| 03:33:46 | 1719 |  17.1 |      11.7 | 0.4232827 | 0.727 |      7 |    12 |  6872 | 0.000397 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
| 03:33:57 | 1721 |   5.8 |      11.7 | 0.4228595 | 0.727 |      0 |    12 |  6880 | 0.000340 |   50000 |
| 03:34:15 | 1722 |  19.0 |      11.7 | 0.4226481 | 0.727 |      5 |    12 |  6884 | 0.000218 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
| 03:34:38 | 1724 |  17.8 |      11.9 | 0.4222256 | 0.727 |     11 |    12 |  6892 | 0.006227 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.727 saved!
| 03:34:55 | 1725 |  16.1 |      11.9 | 0.4220145 | 0.728 |     16 |    12 |  6896 | 0.001582 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.728 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.728 saved!
| 03:35:16 | 1727 |  17.5 |      12.0 | 0.4215926 | 0.728 |     21 |    12 |  6904 | 0.000470 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.728 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.728 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.728 saved!
| 03:35:29 | 1730 |   3.6 |      11.7 | 0.4209605 | 0.728 |      0 |    12 |  6916 | 0.006612 |   50000 |
| 03:35:40 | 1731 |  12.1 |      11.6 | 0.4207500 | 0.728 |      3 |    12 |  6920 | 0.000247 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.728 saved!
| 03:35:57 | 1732 |  19.3 |      11.6 | 0.4205396 | 0.729 |      9 |    12 |  6924 | 0.000646 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.729 saved!
| 03:36:14 | 1733 |  14.5 |      11.7 | 0.4203294 | 0.729 |     13 |    12 |  6928 | 0.000609 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.729 saved!
| 03:36:31 | 1734 |  19.0 |      11.8 | 0.4201192 | 0.729 |     19 |    12 |  6932 | 0.000496 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.729 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.730 saved!
| 03:36:44 | 1736 |   7.5 |      11.7 | 0.4196992 | 0.729 |      0 |    12 |  6940 | 0.012465 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.730 saved!
| 03:37:09 | 1738 |  19.1 |      11.6 | 0.4192796 | 0.730 |      7 |    12 |  6948 | 0.001088 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.730 saved!
| 03:37:24 | 1739 |  17.7 |      11.6 | 0.4190699 | 0.730 |     12 |    12 |  6952 | 0.006008 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.730 saved!
| 03:37:39 | 1740 |  18.2 |      11.7 | 0.4188604 | 0.731 |     17 |    12 |  6956 | 0.001068 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.731 saved!
| 03:37:55 | 1741 |  15.6 |      11.7 | 0.4186510 | 0.731 |     21 |    12 |  6960 | 0.000562 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.731 saved!
| 03:38:13 | 1742 |  20.5 |      11.9 | 0.4184417 | 0.731 |     27 |    12 |  6964 | 0.000314 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745638693.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745638693.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.731 saved!
| 03:38:27 | 1743 |  12.4 |      11.9 | 0.4182324 | 0.731 |      0 |    12 |  6968 | 0.000781 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.731 saved!
| 03:38:43 | 1744 |  14.5 |      12.0 | 0.4180233 | 0.731 |      0 |    12 |  6972 | 0.000534 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.731 saved!
| 03:38:59 | 1745 |  18.1 |      12.0 | 0.4178143 | 0.732 |      5 |    12 |  6976 | 0.000411 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.732 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.732 saved!
| 03:39:22 | 1747 |  17.5 |      12.0 | 0.4173966 | 0.732 |     12 |    12 |  6984 | 0.000659 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.732 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.732 saved!
| 03:39:43 | 1749 |  15.1 |      12.0 | 0.4169793 | 0.733 |     18 |    12 |  6992 | 0.000340 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.733 saved!
| 03:40:00 | 1750 |  13.2 |      12.0 | 0.4167708 | 0.733 |     22 |    12 |  6996 | 0.006054 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1750.keras
✅ Model successfully saved to models/pong_ep1750.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1750
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.733 saved!
| 03:40:19 | 1752 |  17.7 |      12.1 | 0.4163541 | 0.733 |      5 |    12 |  7004 | 0.000754 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.733 saved!
| 03:40:35 | 1753 |  16.1 |      12.2 | 0.4161460 | 0.733 |     10 |    12 |  7008 | 0.000501 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.733 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.733 saved!
| 03:40:56 | 1756 |  17.1 |      12.1 | 0.4155221 | 0.734 |     16 |    12 |  7020 | 0.007324 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.734 saved!
| 03:41:12 | 1757 |  17.1 |      12.2 | 0.4153143 | 0.734 |     21 |    12 |  7024 | 0.000191 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.734 saved!
| 03:41:29 | 1758 |  18.3 |      12.2 | 0.4151066 | 0.734 |     26 |    12 |  7028 | 0.006753 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.734 saved!
| 03:41:45 | 1759 |  19.2 |      12.3 | 0.4148991 | 0.735 |     32 |    12 |  7032 | 0.000476 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.735 saved!
| 03:42:03 | 1760 |  20.5 |      12.5 | 0.4146916 | 0.735 |     37 |    12 |  7036 | 0.001034 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.735 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:42:24 | 1763 |  18.5 |      12.2 | 0.4140699 | 0.735 |      6 |    12 |  7048 | 0.000219 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.735 saved!
| 03:42:43 | 1765 |  20.5 |      12.2 | 0.4136559 | 0.736 |     12 |    12 |  7056 | 0.000269 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.736 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.736 saved!
| 03:43:00 | 1767 |  12.7 |      12.0 | 0.4132424 | 0.736 |      0 |    12 |  7064 | 0.005046 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.736 saved!
| 03:43:16 | 1768 |  20.2 |      12.0 | 0.4130358 | 0.736 |      5 |    12 |  7068 | 0.000324 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745638996.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745638996.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.736 saved!
| 03:43:34 | 1769 |  19.1 |      12.0 | 0.4128293 | 0.736 |     11 |    12 |  7072 | 0.000502 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.736 saved!
| 03:43:52 | 1770 |  18.5 |      12.2 | 0.4126228 | 0.737 |     16 |    12 |  7076 | 0.004582 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.737 saved!
| 03:44:15 | 1772 |  18.4 |      12.1 | 0.4122103 | 0.737 |      5 |    12 |  7084 | 0.000417 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.737 saved!
| 03:44:32 | 1773 |  18.2 |      12.3 | 0.4120042 | 0.737 |     10 |    12 |  7088 | 0.000377 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.737 saved!
| 03:44:48 | 1774 |  18.1 |      12.2 | 0.4117982 | 0.737 |     15 |    12 |  7092 | 0.000659 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.737 saved!
| 03:45:05 | 1775 |  21.2 |      12.4 | 0.4115923 | 0.738 |     21 |    12 |  7096 | 0.006178 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.738 saved!
| 03:45:16 | 1776 |  12.8 |      12.5 | 0.4113865 | 0.738 |     24 |    12 |  7100 | 0.000275 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.738 saved!
| 03:45:29 | 1777 |  15.7 |      12.5 | 0.4111808 | 0.738 |     28 |    12 |  7104 | 0.012804 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.738 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:45:45 | 1778 |  14.2 |      12.5 | 0.4109752 | 0.738 |      0 |    12 |  7108 | 0.000761 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.738 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.738 saved!
| 03:46:03 | 1780 |  15.7 |      12.3 | 0.4105644 | 0.739 |      5 |    12 |  7116 | 0.000952 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.739 saved!
| 03:46:20 | 1781 |  18.7 |      12.3 | 0.4103591 | 0.739 |     11 |    12 |  7120 | 0.007922 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.739 saved!
| 03:46:37 | 1782 |  17.0 |      12.3 | 0.4101539 | 0.739 |     16 |    12 |  7124 | 0.000405 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.739 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.739 saved!
| 03:47:00 | 1784 |  17.1 |      12.2 | 0.4097438 | 0.740 |     22 |    12 |  7132 | 0.005745 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
| 03:47:12 | 1785 |  12.4 |      12.2 | 0.4095390 | 0.740 |      0 |    12 |  7136 | 0.000845 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
| 03:47:23 | 1788 |   1.0 |      11.9 | 0.4089250 | 0.740 |      0 |    12 |  7148 | 0.000280 |   50000 |
| 03:47:35 | 1789 |   8.1 |      11.9 | 0.4087205 | 0.740 |      0 |    12 |  7152 | 0.000573 |   50000 |
| 03:47:46 | 1790 |  12.0 |      11.9 | 0.4085162 | 0.740 |      3 |    12 |  7156 | 0.000626 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
| 03:48:07 | 1792 |  19.2 |      11.9 | 0.4081077 | 0.740 |      9 |    12 |  7164 | 0.000512 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
| 03:48:32 | 1794 |  19.5 |      12.1 | 0.4076997 | 0.740 |     16 |    12 |  7172 | 0.000394 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745639312.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745639312.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.740 saved!
| 03:48:42 | 1795 |  13.0 |      12.2 | 0.4074959 | 0.741 |     19 |    12 |  7176 | 0.000758 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.741 saved!
| 03:49:01 | 1796 |  20.0 |      12.2 | 0.4072921 | 0.741 |     25 |    12 |  7180 | 0.005564 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.741 saved!
| 03:49:17 | 1797 |  17.6 |      12.2 | 0.4070885 | 0.741 |     30 |    12 |  7184 | 0.000557 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.741 saved!
| 03:49:34 | 1798 |  18.2 |      12.3 | 0.4068849 | 0.742 |     35 |    12 |  7188 | 0.000518 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.742 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.742 saved!
| 03:49:49 | 1800 |   6.4 |      12.3 | 0.4064782 | 0.742 |     38 |    12 |  7196 | 0.000372 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1800.keras
✅ Model successfully saved to models/pong_ep1800.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1800
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.742 saved!
✅ Model successfully force-saved to models/pong_milestone_1800.keras
🏆 Milestone save at episode 1800
| 03:50:07 | 1801 |  19.4 |      12.3 | 0.4062749 | 0.742 |     43 |    12 |  7200 | 0.000927 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.742 saved!
| 03:50:18 | 1802 |  12.7 |      12.2 | 0.4060718 | 0.742 |     46 |    12 |  7204 | 0.000454 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.742 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.742 saved!
| 03:50:46 | 1804 |  20.0 |      12.2 | 0.4056658 | 0.743 |     54 |    12 |  7212 | 0.000188 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.743 saved!
| 03:51:00 | 1806 |  12.9 |      12.2 | 0.4052603 | 0.743 |     57 |    12 |  7220 | 0.000474 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.743 saved!
| 03:51:17 | 1809 |  11.9 |      12.1 | 0.4046527 | 0.743 |      0 |    12 |  7232 | 0.000584 |   50000 |
| 03:51:38 | 1811 |  20.2 |      12.2 | 0.4042481 | 0.743 |      6 |    12 |  7240 | 0.000400 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.743 saved!
| 03:52:04 | 1813 |  19.4 |      12.3 | 0.4038440 | 0.743 |      5 |    12 |  7248 | 0.000252 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.743 saved!
| 03:52:22 | 1814 |  20.0 |      12.4 | 0.4036420 | 0.744 |     10 |    12 |  7252 | 0.000652 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.744 saved!
| 03:52:39 | 1815 |  18.2 |      12.6 | 0.4034402 | 0.744 |     15 |    12 |  7256 | 0.000321 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.744 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:52:55 | 1816 |  20.9 |      12.6 | 0.4032385 | 0.744 |     21 |    12 |  7260 | 0.000270 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.744 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:53:08 | 1818 |   8.5 |      12.5 | 0.4028354 | 0.744 |      0 |    12 |  7268 | 0.000429 |   50000 |
| 03:53:24 | 1819 |  17.6 |      12.5 | 0.4026339 | 0.744 |      5 |    12 |  7272 | 0.000445 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.744 saved!
| 03:53:41 | 1820 |  17.8 |      12.6 | 0.4024326 | 0.745 |     10 |    12 |  7276 | 0.000331 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745639621.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745639621.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:53:59 | 1821 |  18.0 |      12.8 | 0.4022314 | 0.745 |     15 |    12 |  7280 | 0.007531 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:54:11 | 1822 |  10.8 |      12.7 | 0.4020303 | 0.745 |      0 |    12 |  7284 | 0.006339 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
| 03:54:25 | 1823 |  14.4 |      12.8 | 0.4018293 | 0.745 |      4 |    12 |  7288 | 0.000809 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
| 03:54:42 | 1825 |  12.5 |      12.6 | 0.4014276 | 0.745 |      0 |    12 |  7296 | 0.007097 |   50000 |
| 03:55:06 | 1827 |  16.2 |      12.6 | 0.4010262 | 0.745 |      0 |    12 |  7304 | 0.000799 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
| 03:55:24 | 1828 |  17.0 |      12.7 | 0.4008257 | 0.745 |      5 |    12 |  7308 | 0.000336 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
| 03:55:34 | 1829 |   9.1 |      12.8 | 0.4006253 | 0.745 |      0 |    12 |  7312 | 0.007932 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.745 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:55:54 | 1831 |  15.1 |      12.8 | 0.4002248 | 0.746 |      5 |    12 |  7320 | 0.005217 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.746 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:56:12 | 1832 |  19.3 |      12.8 | 0.4000247 | 0.746 |     10 |    12 |  7324 | 0.000402 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.746 saved!
| 03:56:31 | 1833 |  16.7 |      12.8 | 0.3998247 | 0.746 |     15 |    12 |  7328 | 0.000634 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.746 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.746 saved!
| 03:56:54 | 1835 |  18.3 |      12.8 | 0.3994249 | 0.747 |     21 |    12 |  7336 | 0.004316 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.747 saved!
| 03:57:11 | 1836 |  18.9 |      12.9 | 0.3992252 | 0.747 |     26 |    12 |  7340 | 0.000334 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.747 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 03:57:24 | 1837 |  16.5 |      13.0 | 0.3990256 | 0.747 |     30 |    12 |  7344 | 0.000553 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.747 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.747 saved!
| 03:57:51 | 1839 |  17.2 |      12.9 | 0.3986267 | 0.748 |     37 |    12 |  7352 | 0.000559 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.748 saved!
| 03:58:18 | 1843 |  21.1 |      12.5 | 0.3978300 | 0.748 |      7 |    12 |  7368 | 0.000358 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.748 saved!
| 03:58:29 | 1845 |   5.8 |      12.3 | 0.3974323 | 0.747 |      0 |    12 |  7376 | 0.000187 |   50000 |
| 03:58:47 | 1846 |  18.7 |      12.4 | 0.3972336 | 0.748 |      5 |    12 |  7380 | 0.006572 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745639927.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745639927.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.748 saved!
| 03:59:05 | 1847 |  18.0 |      12.4 | 0.3970350 | 0.748 |     10 |    12 |  7384 | 0.000475 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.748 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.748 saved!
| 03:59:27 | 1849 |  17.4 |      12.4 | 0.3966380 | 0.748 |     17 |    12 |  7392 | 0.008123 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.748 saved!
| 03:59:46 | 1850 |  18.5 |      12.5 | 0.3964397 | 0.749 |     23 |    12 |  7396 | 0.007402 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1850.keras
✅ Model successfully saved to models/pong_ep1850.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1850
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.749 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.749 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.749 saved!
| 04:00:12 | 1853 |  18.1 |      12.4 | 0.3958453 | 0.749 |     30 |    12 |  7408 | 0.000475 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.749 saved!
| 04:00:28 | 1854 |  18.8 |      12.6 | 0.3956474 | 0.749 |     35 |    12 |  7412 | 0.000198 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.749 saved!
| 04:00:42 | 1855 |  11.8 |      12.6 | 0.3954496 | 0.749 |      0 |    12 |  7416 | 0.000303 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.749 saved!
| 04:01:00 | 1856 |  19.9 |      12.7 | 0.3952519 | 0.750 |      6 |    12 |  7420 | 0.000181 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.750 saved!
| 04:01:22 | 1858 |  21.4 |      12.6 | 0.3948567 | 0.750 |      6 |    12 |  7428 | 0.000475 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.750 saved!
| 04:01:38 | 1859 |  16.9 |      12.6 | 0.3946593 | 0.750 |      0 |    12 |  7432 | 0.000213 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.750 saved!
| 04:01:50 | 1860 |  10.7 |      12.5 | 0.3944620 | 0.750 |      0 |    12 |  7436 | 0.000158 |   50000 |
| 04:02:09 | 1861 |  19.5 |      12.7 | 0.3942647 | 0.750 |      6 |    12 |  7440 | 0.000128 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.750 saved!
| 04:02:26 | 1862 |  20.2 |      12.8 | 0.3940676 | 0.751 |     12 |    12 |  7444 | 0.000334 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.751 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.751 saved!
| 04:02:44 | 1864 |  15.8 |      12.8 | 0.3936736 | 0.751 |     18 |    12 |  7452 | 0.000196 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.751 saved!
| 04:03:02 | 1865 |  20.6 |      12.9 | 0.3934768 | 0.751 |     24 |    12 |  7456 | 0.000186 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.751 saved!
| 04:03:18 | 1866 |  20.1 |      13.0 | 0.3932800 | 0.752 |     30 |    12 |  7460 | 0.007064 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.752 saved!
| 04:03:36 | 1867 |  18.8 |      13.1 | 0.3930834 | 0.752 |     35 |    12 |  7464 | 0.000576 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.752 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:03:48 | 1868 |  12.5 |      13.0 | 0.3928869 | 0.752 |     38 |    12 |  7468 | 0.000523 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745640228.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745640228.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.752 saved!
| 04:04:07 | 1869 |  17.5 |      13.0 | 0.3926904 | 0.752 |     43 |    12 |  7472 | 0.004949 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.752 saved!
| 04:04:26 | 1870 |  17.3 |      13.0 | 0.3924941 | 0.753 |     48 |    12 |  7476 | 0.000358 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.753 saved!
| 04:04:37 | 1871 |  11.8 |      13.1 | 0.3922978 | 0.753 |     51 |    12 |  7480 | 0.006530 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.753 saved!
| 04:04:53 | 1872 |  15.0 |      13.0 | 0.3921017 | 0.753 |      0 |    12 |  7484 | 0.000530 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.753 saved!
| 04:05:09 | 1873 |  15.6 |      13.0 | 0.3919056 | 0.753 |      0 |    12 |  7488 | 0.000510 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.753 saved!
| 04:05:26 | 1874 |  14.5 |      13.0 | 0.3917097 | 0.753 |      4 |    12 |  7492 | 0.000445 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.753 saved!
| 04:05:41 | 1875 |  15.2 |      12.9 | 0.3915138 | 0.753 |      8 |    12 |  7496 | 0.000429 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.753 saved!
| 04:05:59 | 1876 |  18.9 |      13.0 | 0.3913181 | 0.754 |     13 |    12 |  7500 | 0.000252 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
| 04:06:09 | 1879 |   2.0 |      12.7 | 0.3907314 | 0.754 |     15 |    12 |  7512 | 0.000162 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
| 04:06:29 | 1882 |   8.3 |      12.4 | 0.3901456 | 0.754 |      0 |    12 |  7524 | 0.000213 |   50000 |
| 04:06:47 | 1883 |  20.6 |      12.6 | 0.3899505 | 0.754 |      6 |    12 |  7528 | 0.000279 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
| 04:07:03 | 1884 |  15.2 |      12.6 | 0.3897555 | 0.754 |      0 |    12 |  7532 | 0.000216 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
| 04:07:20 | 1885 |  18.3 |      12.6 | 0.3895607 | 0.754 |      5 |    12 |  7536 | 0.000228 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.754 saved!
| 04:07:43 | 1888 |  18.2 |      12.7 | 0.3889766 | 0.755 |     11 |    12 |  7548 | 0.000203 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.755 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.755 saved!
| 04:08:01 | 1890 |   8.5 |      12.8 | 0.3885877 | 0.755 |     16 |    12 |  7556 | 0.000110 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.755 saved!
| 04:08:11 | 1892 |   5.1 |      12.6 | 0.3881992 | 0.755 |      1 |    12 |  7564 | 0.000274 |   50000 |
| 04:08:37 | 1894 |  20.9 |      12.6 | 0.3878111 | 0.755 |      8 |    12 |  7572 | 0.000190 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.755 saved!
| 04:08:56 | 1896 |  20.9 |      12.5 | 0.3874234 | 0.755 |      6 |    12 |  7580 | 0.000229 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745640536.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745640536.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.755 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.756 saved!
| 04:09:08 | 1898 |   9.9 |      12.3 | 0.3870361 | 0.756 |      9 |    12 |  7588 | 0.000172 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.756 saved!
| 04:09:26 | 1899 |  19.0 |      12.4 | 0.3868426 | 0.756 |     14 |    12 |  7592 | 0.000230 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.756 saved!
| 04:09:43 | 1900 |  18.5 |      12.5 | 0.3866492 | 0.756 |     19 |    12 |  7596 | 0.000247 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1900.keras
✅ Model successfully saved to models/pong_ep1900.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1900
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.756 saved!
| 04:09:55 | 1901 |  12.1 |      12.4 | 0.3864558 | 0.756 |     22 |    12 |  7600 | 0.000391 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.756 saved!
| 04:10:13 | 1902 |  18.1 |      12.5 | 0.3862626 | 0.757 |     27 |    12 |  7604 | 0.000519 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
| 04:10:25 | 1904 |   5.7 |      12.3 | 0.3858764 | 0.757 |     29 |    12 |  7612 | 0.000152 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
| 04:10:50 | 1906 |  17.0 |      12.4 | 0.3854907 | 0.757 |     35 |    12 |  7620 | 0.000257 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
| 04:11:03 | 1907 |  12.6 |      12.5 | 0.3852979 | 0.757 |     38 |    12 |  7624 | 0.000416 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
| 04:11:20 | 1908 |  16.5 |      12.6 | 0.3851053 | 0.757 |     42 |    12 |  7628 | 0.000269 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.757 saved!
| 04:11:37 | 1909 |  19.7 |      12.7 | 0.3849127 | 0.758 |     48 |    12 |  7632 | 0.000314 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.758 saved!
| 04:11:47 | 1910 |  10.5 |      12.7 | 0.3847203 | 0.758 |     50 |    12 |  7636 | 0.000157 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.758 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.758 saved!
| 04:12:09 | 1912 |  12.8 |      12.7 | 0.3843356 | 0.758 |     55 |    12 |  7644 | 0.000396 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.758 saved!
| 04:12:29 | 1913 |  20.4 |      12.7 | 0.3841435 | 0.758 |     61 |    12 |  7648 | 0.000539 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.758 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.758 saved!
| 04:12:52 | 1915 |  19.6 |      12.6 | 0.3837594 | 0.759 |     67 |    12 |  7656 | 0.000588 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.759 saved!
| 04:13:11 | 1916 |  17.4 |      12.5 | 0.3835675 | 0.759 |     72 |    12 |  7660 | 0.000688 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.759 saved!
| 04:13:31 | 1917 |  19.5 |      12.7 | 0.3833757 | 0.759 |     77 |    12 |  7664 | 0.000312 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.759 saved!
| 04:13:51 | 1918 |  21.1 |      12.9 | 0.3831841 | 0.759 |     83 |    12 |  7668 | 0.000467 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.759 saved!
| 04:14:10 | 1919 |  20.6 |      12.9 | 0.3829925 | 0.760 |     88 |    12 |  7672 | 0.000405 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745640850.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745640850.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.760 saved!
| 04:14:32 | 1920 |  18.8 |      12.9 | 0.3828010 | 0.760 |     93 |    12 |  7676 | 0.006863 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.760 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.760 saved!
| 04:14:47 | 1922 |   4.2 |      12.7 | 0.3824183 | 0.760 |     96 |    12 |  7684 | 0.000487 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.760 saved!
| 04:15:00 | 1923 |  12.5 |      12.7 | 0.3822271 | 0.760 |     99 |    12 |  7688 | 0.000194 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.760 saved!
| 04:15:20 | 1924 |  21.0 |      12.9 | 0.3820359 | 0.761 |    105 |    12 |  7692 | 0.000165 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.761 saved!
| 04:15:33 | 1925 |  13.7 |      12.9 | 0.3818449 | 0.761 |    108 |    12 |  7696 | 0.000163 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.761 saved!
| 04:15:49 | 1926 |  17.2 |      13.0 | 0.3816540 | 0.761 |    112 |    12 |  7700 | 0.000308 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.761 saved!
| 04:16:07 | 1927 |  20.1 |      13.0 | 0.3814632 | 0.761 |    118 |    12 |  7704 | 0.000125 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.761 saved!
| 04:16:17 | 1928 |   5.5 |      12.9 | 0.3812724 | 0.761 |      0 |    12 |  7708 | 0.000415 |   50000 |
| 04:16:38 | 1929 |  18.0 |      13.0 | 0.3810818 | 0.761 |      5 |    12 |  7712 | 0.000364 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.761 saved!
| 04:16:52 | 1930 |   9.6 |      13.1 | 0.3808913 | 0.761 |      7 |    12 |  7716 | 0.006695 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.761 saved!
| 04:17:11 | 1931 |  18.6 |      13.1 | 0.3807008 | 0.762 |      0 |    12 |  7720 | 0.000535 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.762 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:17:24 | 1933 |   5.3 |      12.8 | 0.3803202 | 0.761 |      0 |    12 |  7728 | 0.000311 |   50000 |
| 04:17:43 | 1934 |  21.3 |      13.0 | 0.3801301 | 0.762 |      6 |    12 |  7732 | 0.000625 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.762 saved!
| 04:18:05 | 1936 |  19.8 |      12.8 | 0.3797500 | 0.762 |      6 |    12 |  7740 | 0.000177 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.762 saved!
| 04:18:22 | 1937 |  20.6 |      12.9 | 0.3795601 | 0.762 |     11 |    12 |  7744 | 0.000511 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.762 saved!
| 04:18:39 | 1938 |  16.2 |      12.9 | 0.3793704 | 0.762 |     15 |    12 |  7748 | 0.000294 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.762 saved!
| 04:18:59 | 1939 |  21.5 |      13.0 | 0.3791807 | 0.762 |     21 |    12 |  7752 | 0.000341 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.762 saved!
| 04:19:19 | 1940 |  19.7 |      13.2 | 0.3789911 | 0.763 |     26 |    12 |  7756 | 0.007699 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745641159.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745641159.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.763 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:19:38 | 1941 |  19.9 |      13.3 | 0.3788016 | 0.763 |     32 |    12 |  7760 | 0.012772 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.763 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:19:48 | 1942 |  10.0 |      13.4 | 0.3786122 | 0.763 |     34 |    12 |  7764 | 0.000860 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.763 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:20:07 | 1943 |  20.9 |      13.4 | 0.3784229 | 0.763 |     40 |    12 |  7768 | 0.007087 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.763 saved!
| 04:20:25 | 1944 |  18.1 |      13.6 | 0.3782337 | 0.764 |      0 |    12 |  7772 | 0.001083 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.764 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:20:40 | 1945 |  16.2 |      13.7 | 0.3780446 | 0.764 |      4 |    12 |  7776 | 0.012147 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.764 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:20:56 | 1946 |  15.6 |      13.6 | 0.3778555 | 0.764 |      8 |    12 |  7780 | 0.001939 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.764 saved!
| 04:21:07 | 1947 |   9.8 |      13.6 | 0.3776666 | 0.764 |     10 |    12 |  7784 | 0.000842 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.764 saved!
| 04:21:23 | 1948 |  13.1 |      13.6 | 0.3774778 | 0.764 |      0 |    12 |  7788 | 0.000770 |   50000 |
| 04:21:45 | 1949 |  17.3 |      13.6 | 0.3772890 | 0.764 |      5 |    12 |  7792 | 0.000671 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.764 saved!
| 04:22:05 | 1950 |  18.6 |      13.6 | 0.3771004 | 0.764 |     10 |    12 |  7796 | 0.000348 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep1950.keras
✅ Model successfully saved to models/pong_ep1950.keras (231.1 KB)
📊 Episode checkpoint saved at episode 1950
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.764 saved!
| 04:22:24 | 1951 |  18.6 |      13.7 | 0.3769118 | 0.765 |     15 |    12 |  7800 | 0.000801 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.765 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.765 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:22:39 | 1953 |   4.1 |      13.7 | 0.3765350 | 0.765 |      0 |    12 |  7808 | 0.006850 |   50000 |
| 04:23:01 | 1954 |  15.7 |      13.6 | 0.3763468 | 0.765 |      4 |    12 |  7812 | 0.000554 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.765 saved!
| 04:23:21 | 1955 |  19.0 |      13.7 | 0.3761586 | 0.765 |      9 |    12 |  7816 | 0.000472 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.765 saved!
| 04:23:40 | 1956 |  21.6 |      13.7 | 0.3759705 | 0.765 |     14 |    12 |  7820 | 0.000533 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.765 saved!
| 04:24:00 | 1957 |  18.0 |      13.8 | 0.3757825 | 0.766 |     19 |    12 |  7824 | 0.000266 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.766 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:24:17 | 1958 |  20.1 |      13.8 | 0.3755946 | 0.766 |     25 |    12 |  7828 | 0.000294 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.766 saved!
| 04:24:36 | 1959 |  21.0 |      13.9 | 0.3754068 | 0.766 |     30 |    12 |  7832 | 0.000328 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745641476.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745641476.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.766 saved!
✅ Model successfully force-saved to models/pong_best_score.keras
| 04:24:58 | 1961 |  20.0 |      13.8 | 0.3750315 | 0.766 |     36 |    12 |  7840 | 0.000239 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.766 saved!
| 04:25:13 | 1963 |   9.5 |      13.6 | 0.3746566 | 0.766 |      2 |    12 |  7848 | 0.000301 |   50000 |
| 04:25:33 | 1964 |  17.0 |      13.6 | 0.3744693 | 0.767 |      7 |    12 |  7852 | 0.007399 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.767 saved!
| 04:25:53 | 1965 |  17.8 |      13.6 | 0.3742820 | 0.767 |     12 |    12 |  7856 | 0.000299 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.767 saved!
| 04:26:12 | 1966 |  13.7 |      13.5 | 0.3740949 | 0.767 |     16 |    12 |  7860 | 0.006622 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.767 saved!
| 04:26:34 | 1968 |  14.0 |      13.4 | 0.3737209 | 0.767 |      4 |    12 |  7868 | 0.000734 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.767 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.767 saved!
| 04:26:58 | 1970 |  17.6 |      13.2 | 0.3733472 | 0.767 |     10 |    12 |  7876 | 0.000329 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.767 saved!
| 04:27:20 | 1971 |  18.5 |      13.3 | 0.3731606 | 0.768 |     15 |    12 |  7880 | 0.000282 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.768 saved!
| 04:27:40 | 1972 |  20.8 |      13.4 | 0.3729740 | 0.768 |     21 |    12 |  7884 | 0.000152 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.768 saved!
| 04:28:02 | 1973 |  19.2 |      13.4 | 0.3727875 | 0.768 |     26 |    12 |  7888 | 0.000301 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.768 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.768 saved!
| 04:28:16 | 1975 |   1.4 |      13.2 | 0.3724148 | 0.768 |      0 |    12 |  7896 | 0.000195 |   50000 |
| 04:28:29 | 1977 |  13.9 |      13.1 | 0.3720425 | 0.768 |      3 |    12 |  7904 | 0.000367 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.768 saved!
| 04:28:47 | 1979 |  13.0 |      13.3 | 0.3716705 | 0.768 |      0 |    12 |  7912 | 0.000411 |   50000 |
| 04:29:05 | 1980 |  20.7 |      13.4 | 0.3714847 | 0.768 |      5 |    12 |  7916 | 0.000203 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.768 saved!
| 04:29:23 | 1981 |  17.9 |      13.5 | 0.3712990 | 0.769 |     10 |    12 |  7920 | 0.000249 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
| 04:29:33 | 1982 |  12.0 |      13.6 | 0.3711133 | 0.769 |     13 |    12 |  7924 | 0.000206 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
| 04:29:47 | 1983 |  16.9 |      13.5 | 0.3709278 | 0.769 |     17 |    12 |  7928 | 0.000140 |   50000 |
✅ Model successfully force-saved to models/pong_time_1745641787.keras
⏱️ Time-based checkpoint saved at models/pong_time_1745641787.keras
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
| 04:30:06 | 1986 |  11.6 |      13.4 | 0.3703716 | 0.769 |      0 |    12 |  7940 | 0.000171 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
| 04:30:28 | 1989 |  13.6 |      13.2 | 0.3698164 | 0.769 |      0 |    12 |  7952 | 0.000237 |   50000 |
| 04:30:50 | 1991 |  18.4 |      13.3 | 0.3694466 | 0.769 |      6 |    12 |  7960 | 0.000250 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
| 04:31:04 | 1993 |   6.3 |      13.3 | 0.3690773 | 0.769 |      0 |    12 |  7968 | 0.000171 |   50000 |
| 04:31:22 | 1994 |  19.7 |      13.3 | 0.3688927 | 0.769 |      5 |    12 |  7972 | 0.000163 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.769 saved!
| 04:31:33 | 1995 |  12.3 |      13.4 | 0.3687083 | 0.770 |      8 |    12 |  7976 | 0.000330 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.770 saved!
| 04:31:52 | 1996 |  21.2 |      13.4 | 0.3685239 | 0.770 |     13 |    12 |  7980 | 0.000173 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.770 saved!
| 04:32:08 | 1997 |  17.1 |      13.6 | 0.3683397 | 0.770 |     17 |    12 |  7984 | 0.000163 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.770 saved!
| 04:32:26 | 1998 |  18.9 |      13.7 | 0.3681555 | 0.770 |      0 |    12 |  7988 | 0.000251 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.770 saved!
| 04:32:44 | 1999 |  18.3 |      13.6 | 0.3679714 | 0.770 |      5 |    12 |  7992 | 0.000243 |   50000 |
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.770 saved!
| 04:33:02 | 2000 |  18.5 |      13.6 | 0.3677875 | 0.770 |     10 |    12 |  7996 | 0.000121 |   50000 |
Attempting to save model to: /kaggle/working/models/pong_ep2000.keras
✅ Model successfully saved to models/pong_ep2000.keras (231.1 KB)
📊 Episode checkpoint saved at episode 2000
✅ Model successfully force-saved to models/pong_best_hitrate.keras

⭐ New best hit rate: 0.770 saved!
✅ Model successfully force-saved to models/pong_milestone_2000.keras
🏆 Milestone save at episode 2000

================================================================================
Training complete after 2000 episodes!
Total time: 222.3 minutes
Final hit rate: 0.770
Best hit rate achieved: 0.770
Total hits: 3884, Total misses: 1157
================================================================================
✅ Model successfully force-saved to models/pong_final.keras

Training process complete!
Final hit rate: 0.770
Your TFLite model is ready for use in your Flutter app!

=== FINAL STATUS CHECK ===
Files in models: ['pong_ep1450.keras', 'pong_ep1400.keras', 'pong_time_1745641787.keras', 'pong_ep950.keras', 'pong_milestone_1800.keras', 'pong_ep1250.keras', 'pong_time_1745630459.keras', 'pong_time_1745632891.keras', 'pong_time_1745637470.keras', 'pong_milestone_2000.keras', 'pong_time_1745630157.keras', 'pong_time_1745638085.keras', 'pong_milestone_200.keras', 'pong_milestone_400.keras', 'pong_time_1745638389.keras', 'pong_time_1745640536.keras', 'pong_ep1100.keras', 'pong_time_1745640850.keras', 'pong_ep800.keras', 'pong_ep1050.keras', 'pong_time_1745637774.keras', 'pong_time_1745629549.keras', 'pong_ep1300.keras', 'pong_time_1745639927.keras', 'pong_ep150.keras', 'pong_time_1745632590.keras', 'pong_time_1745636553.keras', 'pong_milestone_1600.keras', 'pong_ep1350.keras', 'pong_ep650.keras', 'pong_ep2000.keras', 'pong_ep500.keras', 'pong_time_1745634719.keras', 'pong_ep700.keras', 'pong_ep1550.keras', 'pong_time_1745628947.keras', 'pong_time_1745634113.keras', 'pong_time_1745641476.keras', 'pong_time_1745633812.keras', 'pong_ep1950.keras', 'pong_time_1745635949.keras', 'pong_time_1745641159.keras', 'pong_milestone_1200.keras', 'pong_time_1745639621.keras', 'pong_time_1745629850.keras', 'pong_time_1745633195.keras', 'pong_ep1650.keras', 'pong_ep400.keras', 'pong_ep1900.keras', 'pong_ep1750.keras', 'pong_ep50.keras', 'pong_best_score.keras', 'pong_ep200.keras', 'pong_ep250.keras', 'pong_ep1850.keras', 'pong_ep100.keras', 'pong_ep1600.keras', 'pong_ep1150.keras', 'pong_time_1745639312.keras', 'pong_ep1800.keras', 'pong_time_1745633498.keras', 'pong_milestone_600.keras', 'pong_ep1500.keras', 'pong_time_1745640228.keras', 'pong_final.keras', 'pong_time_1745630765.keras', 'pong_time_1745629247.keras', 'pong_ep550.keras', 'pong_ep300.keras', 'pong_time_1745632287.keras', 'pong_time_1745634415.keras', 'pong_milestone_1000.keras', 'pong_milestone_1400.keras', 'pong_ep1200.keras', 'pong_time_1745631676.keras', 'pong_time_1745635030.keras', 'pong_ep1700.keras', 'pong_ep600.keras', 'pong_time_1745631980.keras', 'pong_ep450.keras', 'pong_best_hitrate.keras', 'pong_time_1745635643.keras', 'pong_time_1745636860.keras', 'pong_milestone_800.keras', 'pong_time_1745636251.keras', 'pong_ep350.keras', 'pong_time_1745635332.keras', 'pong_ep1000.keras', 'pong_ep750.keras', 'pong_time_1745638996.keras', 'pong_time_1745631068.keras', 'pong_time_1745637161.keras', 'pong_ep900.keras', 'pong_ep850.keras', 'pong_time_1745631375.keras', 'pong_time_1745638693.keras']
Files in /kaggle/working: []
Files in /tmp: []
TFLite model not found in any location!

Training Complete! Don't forget to generate your pong_ai_model.tflite file from tflite_converter.py.
