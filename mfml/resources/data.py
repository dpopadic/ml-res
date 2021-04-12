import numpy as np
x = np.array([[ 0.  ,  0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,
         0.09,  0.1 ,  0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,
         0.18,  0.19,  0.2 ,  0.21,  0.22,  0.23,  0.24,  0.25,  0.26,
         0.27,  0.28,  0.29,  0.3 ,  0.31,  0.32,  0.33,  0.34,  0.35,
         0.36,  0.37,  0.38,  0.39,  0.4 ,  0.41,  0.42,  0.43,  0.44,
         0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ,  0.51,  0.52,  0.53,
         0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ,  0.61,  0.62,
         0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ,  0.71,
         0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ,
         0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,
         0.9 ,  0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,
         0.99]])


y = np.array([[ 0.5       ,  0.50009902,  0.50078751,  0.50263171,  0.50615226,
         0.5118034 ,  0.51995466,  0.53087547,  0.54472343,  0.56153657,
         0.58122992,  0.60359653,  0.62831281,  0.65494819,  0.68297861,
         0.7118034 ,  0.74076505,  0.76917106,  0.7963171 ,  0.82151087,
         0.84409548,  0.86347181,  0.87911897,  0.89061206,  0.89763674,
         0.9       ,  0.89763674,  0.89061206,  0.87911897,  0.86347181,
         0.84409548,  0.82151087,  0.7963171 ,  0.76917106,  0.74076505,
         0.7118034 ,  0.68297861,  0.65494819,  0.62831281,  0.60359653,
         0.58122992,  0.56153657,  0.54472343,  0.53087547,  0.51995466,
         0.5118034 ,  0.50615226,  0.50263171,  0.50078751,  0.50009902,
         0.5       ,  0.49990098,  0.49921249,  0.49736829,  0.49384774,
         0.4881966 ,  0.48004534,  0.46912453,  0.45527657,  0.43846343,
         0.41877008,  0.39640347,  0.37168719,  0.34505181,  0.31702139,
         0.2881966 ,  0.25923495,  0.23082894,  0.2036829 ,  0.17848913,
         0.15590452,  0.13652819,  0.12088103,  0.10938794,  0.10236326,
         0.1       ,  0.10236326,  0.10938794,  0.12088103,  0.13652819,
         0.15590452,  0.17848913,  0.2036829 ,  0.23082894,  0.25923495,
         0.2881966 ,  0.31702139,  0.34505181,  0.37168719,  0.39640347,
         0.41877008,  0.43846343,  0.45527657,  0.46912453,  0.48004534,
         0.4881966 ,  0.49384774,  0.49736829,  0.49921249,  0.49990098],
       [ 0.625     ,  0.62701541,  0.63296789,  0.64258068,  0.65540709,
         0.67085156,  0.68819755,  0.70664083,  0.72532628,  0.74338643,
         0.75997967,  0.77432624,  0.78574006,  0.79365515,  0.79764521,
         0.79743558,  0.79290745,  0.78409411,  0.77116996,  0.75443315,
         0.73428307,  0.71119423,  0.68568811,  0.65830476,  0.62957574,
         0.6       ,  0.57002377,  0.5400257 ,  0.51030758,  0.4810911 ,
         0.45252033,  0.42466948,  0.3975551 ,  0.37115155,  0.34540857,
         0.32026952,  0.29568895,  0.27164821,  0.24816805,  0.22531726,
         0.20321693,  0.18203995,  0.16200599,  0.14337224,  0.12642077,
         0.11144335,  0.0987249 ,  0.08852676,  0.08107098,  0.07652676,
         0.075     ,  0.07652676,  0.08107098,  0.08852676,  0.0987249 ,
         0.11144335,  0.12642077,  0.14337224,  0.16200599,  0.18203995,
         0.20321693,  0.22531726,  0.24816805,  0.27164821,  0.29568895,
         0.32026952,  0.34540857,  0.37115155,  0.3975551 ,  0.42466948,
         0.45252033,  0.4810911 ,  0.51030758,  0.5400257 ,  0.57002377,
         0.6       ,  0.62957574,  0.65830476,  0.68568811,  0.71119423,
         0.73428307,  0.75443315,  0.77116996,  0.78409411,  0.79290745,
         0.79743558,  0.79764521,  0.79365515,  0.78574006,  0.77432624,
         0.75997967,  0.74338643,  0.72532628,  0.70664083,  0.68819755,
         0.67085156,  0.65540709,  0.64258068,  0.63296789,  0.62701541]])


x_heights = np.array([  51.25,   53.75,   56.25,   58.75,   61.25,   63.75,   66.25,
                        68.75,   71.25,   73.75,   76.25,   78.75,   81.25,   83.75,
                        86.25,   88.75,   91.25,   93.75,   96.25,   98.75,  101.25,
                        103.75,  106.25,  108.75,  111.25,  113.75,  116.25,  118.75,
                        121.25,  123.75,  126.25,  128.75,  131.25,  133.75,  136.25,
                        138.75,  141.25,  143.75,  146.25,  148.75,  151.25,  153.75,
                        156.25,  158.75,  161.25,  163.75,  166.25,  168.75,  171.25,
                        173.75,  176.25,  178.75,  181.25,  183.75,  186.25,  188.75,
                        191.25,  193.75,  196.25,  198.75,  201.25,  203.75,  206.25,
                        208.75,  211.25,  213.75,  216.25,  218.75,  221.25,  223.75,
                        226.25,  228.75,  231.25,  233.75,  236.25,  238.75,  241.25,
                        243.75,  246.25,  248.75,  251.25,  253.75,  256.25,  258.75,
                        261.25,  263.75,  266.25,  268.75,  271.25,  273.75,  276.25,
                        278.75,  281.25,  283.75,  286.25,  288.75,  291.25,  293.75,
                        296.25,  298.75])

y_heights = np.array([  0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.01246231,
                        0.00522613,  0.00924623,  0.02572864,  0.02613065,  0.05065327,
                        0.05306533,  0.05105528,  0.04542714,  0.03658291,  0.04221106,
                        0.0201005 ,  0.00723618,  0.00723618,  0.00723618,  0.00040201,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
                        0.        ,  0.        ,  0.        ,  0.        ,  0.        ])

