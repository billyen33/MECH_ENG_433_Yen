import matplotlib.pyplot as plt
import numpy as np
import csv
title1 = "Sampling rate=1000 Hz, fL=30Hz, bL=10Hz, Hamming"
title2 = "Sampling rate=10 Hz, fL=0.2Hz, bL=0.1Hz, Hamming"
title3 = "Sampling rate=10 Hz, fL=0.5Hz, bL=0.1Hz, Hamming"
title4 = "Sampling rate=20 Hz, fL=1Hz, bL=1Hz, Blackman"
x2 = 300
x3 = 100
x4 = 300

h1 = [
    -0.000132798787597033,
    -0.000113230491342199,
    -0.000089525709484090,
    -0.000062274459193230,
    -0.000032169432150192,
    0.000000000000000000,
    0.000033355701444144,
    0.000066941374212968,
    0.000099736582136789,
    0.000130674824763770,
    0.000158666104632901,
    0.000182624176482642,
    0.000201498353711713,
    0.000214309391946868,
    0.000220188591954083,
    0.000218418887197329,
    0.000208476329574007,
    0.000190070085020710,
    0.000163178822491537,
    0.000128081246492911,
    0.000085378502338976,
    0.000036006287000502,
    -0.000018765266692041,
    -0.000077345498914801,
    -0.000137852001826465,
    -0.000198154747274918,
    -0.000255935355801612,
    -0.000308760553420701,
    -0.000354168089305704,
    -0.000389762623545822,
    -0.000413318378416672,
    -0.000422884718480641,
    -0.000416890322165748,
    -0.000394241264736357,
    -0.000354408178935123,
    -0.000297497717179978,
    -0.000224303821650625,
    -0.000136334819803447,
    -0.000035813096243060,
    0.000074354969919425,
    0.000190639998092623,
    0.000308981471688507,
    0.000424909072359708,
    0.000533690695552720,
    0.000630502997431586,
    0.000710619043911200,
    0.000769606498536874,
    0.000803528856758816,
    0.000809141563862167,
    0.000784074488393560,
    0.000726992197746387,
    0.000637723820269968,
    0.000517354987076206,
    0.000368275419299074,
    0.000194177139512019,
    -0.000000000000000001,
    -0.000208176818780752,
    -0.000423296546872232,
    -0.000637536769140050,
    -0.000842566293383057,
    -0.001029839491466513,
    -0.001190918670080399,
    -0.001317813303812381,
    -0.001403323594260202,
    -0.001441374880957194,
    -0.001427328985199082,
    -0.001358258661626316,
    -0.001233171990065951,
    -0.001053174765354344,
    -0.000821560716397402,
    -0.000543821665100629,
    -0.000227572455951380,
    0.000117611438098335,
    0.000480442402756446,
    0.000848250576254220,
    0.001207387008193570,
    0.001543688623089155,
    0.001842990484638568,
    0.002091668221436030,
    0.002277191371488665,
    0.002388666939876700,
    0.002417351729436592,
    0.002357112062159539,
    0.002204810394774631,
    0.001960600050805263,
    0.001628111816249282,
    0.001214519417585557,
    0.000730474828329415,
    0.000189908813990695,
    -0.000390303020500041,
    -0.000990803338673059,
    -0.001590334873549434,
    -0.002166425489301062,
    -0.002696156443824052,
    -0.003156989697021943,
    -0.003527626721989410,
    -0.003788868753235084,
    -0.003924446878128356,
    -0.003921789943457690,
    -0.003772698970066666,
    -0.003473898666249611,
    -0.003027439683523686,
    -0.002440929401763047,
    -0.001727574157238741,
    -0.000906021789676765,
    0.000000000000000002,
    0.000962246934370886,
    0.001948713281714058,
    0.002924561802190979,
    0.003853204604660524,
    0.004697504666491464,
    0.005421062245152956,
    0.005989545921600572,
    0.006372024756005265,
    0.006542256163118335,
    0.006479883740204743,
    0.006171500468157106,
    0.005611535466122477,
    0.004802926766783689,
    0.003757548293579066,
    0.002496366210160408,
    0.001049307875170985,
    -0.000545164471906975,
    -0.002240773724639597,
    -0.003984430365222750,
    -0.005717496491033319,
    -0.007377281331777585,
    -0.008898729691156071,
    -0.010216257288837603,
    -0.011265680823470969,
    -0.011986185962655899,
    -0.012322273581213858,
    -0.012225623550017845,
    -0.011656816298980202,
    -0.010586855250471114,
    -0.008998437988878647,
    -0.006886930578954189,
    -0.004261007589090757,
    -0.001142929878407450,
    0.002431557218054777,
    0.006413711350211376,
    0.010742660592668754,
    0.015346633468844165,
    0.020144522801346050,
    0.025047744002528655,
    0.029962338878956499,
    0.034791267891136582,
    0.039436827362158720,
    0.043803123589841543,
    0.047798533349824264,
    0.051338079978248644,
    0.054345656118302887,
    0.056756028259283380,
    0.058516564273729282,
    0.059588633084325673,
    0.059948635123203697,
    0.059588633084325673,
    0.058516564273729282,
    0.056756028259283380,
    0.054345656118302887,
    0.051338079978248644,
    0.047798533349824264,
    0.043803123589841550,
    0.039436827362158720,
    0.034791267891136582,
    0.029962338878956499,
    0.025047744002528655,
    0.020144522801346054,
    0.015346633468844165,
    0.010742660592668754,
    0.006413711350211377,
    0.002431557218054777,
    -0.001142929878407450,
    -0.004261007589090758,
    -0.006886930578954189,
    -0.008998437988878649,
    -0.010586855250471114,
    -0.011656816298980202,
    -0.012225623550017845,
    -0.012322273581213856,
    -0.011986185962655901,
    -0.011265680823470969,
    -0.010216257288837603,
    -0.008898729691156073,
    -0.007377281331777586,
    -0.005717496491033321,
    -0.003984430365222751,
    -0.002240773724639597,
    -0.000545164471906975,
    0.001049307875170985,
    0.002496366210160408,
    0.003757548293579066,
    0.004802926766783690,
    0.005611535466122478,
    0.006171500468157107,
    0.006479883740204743,
    0.006542256163118338,
    0.006372024756005267,
    0.005989545921600573,
    0.005421062245152955,
    0.004697504666491463,
    0.003853204604660523,
    0.002924561802190979,
    0.001948713281714058,
    0.000962246934370886,
    0.000000000000000002,
    -0.000906021789676765,
    -0.001727574157238742,
    -0.002440929401763047,
    -0.003027439683523685,
    -0.003473898666249611,
    -0.003772698970066666,
    -0.003921789943457690,
    -0.003924446878128358,
    -0.003788868753235084,
    -0.003527626721989410,
    -0.003156989697021944,
    -0.002696156443824053,
    -0.002166425489301063,
    -0.001590334873549434,
    -0.000990803338673059,
    -0.000390303020500041,
    0.000189908813990695,
    0.000730474828329416,
    0.001214519417585558,
    0.001628111816249283,
    0.001960600050805264,
    0.002204810394774631,
    0.002357112062159539,
    0.002417351729436594,
    0.002388666939876701,
    0.002277191371488665,
    0.002091668221436030,
    0.001842990484638568,
    0.001543688623089156,
    0.001207387008193570,
    0.000848250576254220,
    0.000480442402756446,
    0.000117611438098335,
    -0.000227572455951380,
    -0.000543821665100629,
    -0.000821560716397402,
    -0.001053174765354344,
    -0.001233171990065951,
    -0.001358258661626316,
    -0.001427328985199083,
    -0.001441374880957195,
    -0.001403323594260202,
    -0.001317813303812381,
    -0.001190918670080400,
    -0.001029839491466514,
    -0.000842566293383057,
    -0.000637536769140050,
    -0.000423296546872232,
    -0.000208176818780752,
    -0.000000000000000001,
    0.000194177139512019,
    0.000368275419299074,
    0.000517354987076206,
    0.000637723820269969,
    0.000726992197746387,
    0.000784074488393561,
    0.000809141563862167,
    0.000803528856758816,
    0.000769606498536874,
    0.000710619043911200,
    0.000630502997431587,
    0.000533690695552721,
    0.000424909072359708,
    0.000308981471688507,
    0.000190639998092623,
    0.000074354969919425,
    -0.000035813096243060,
    -0.000136334819803447,
    -0.000224303821650625,
    -0.000297497717179978,
    -0.000354408178935124,
    -0.000394241264736357,
    -0.000416890322165748,
    -0.000422884718480641,
    -0.000413318378416672,
    -0.000389762623545822,
    -0.000354168089305705,
    -0.000308760553420701,
    -0.000255935355801612,
    -0.000198154747274918,
    -0.000137852001826465,
    -0.000077345498914802,
    -0.000018765266692041,
    0.000036006287000502,
    0.000085378502338976,
    0.000128081246492911,
    0.000163178822491537,
    0.000190070085020710,
    0.000208476329574007,
    0.000218418887197329,
    0.000220188591954083,
    0.000214309391946868,
    0.000201498353711713,
    0.000182624176482642,
    0.000158666104632901,
    0.000130674824763770,
    0.000099736582136789,
    0.000066941374212968,
    0.000033355701444144,
    0.000000000000000000,
    -0.000032169432150192,
    -0.000062274459193230,
    -0.000089525709484090,
    -0.000113230491342199,
    -0.000132798787597033,
]

h2 = [
    0.000096734265968441,
    0.000079893284958558,
    0.000061665650631385,
    0.000042179215242215,
    0.000021572900859564,
    0.000000000000000000,
    -0.000022368415985591,
    -0.000045340171044719,
    -0.000068698938714455,
    -0.000092201675432196,
    -0.000115576726591127,
    -0.000138522787525481,
    -0.000160708883789383,
    -0.000181775511282445,
    -0.000201337047432889,
    -0.000218985510390935,
    -0.000234295704773932,
    -0.000246831750834351,
    -0.000256154949999036,
    -0.000261832894650648,
    -0.000263449684954200,
    -0.000260617071676855,
    -0.000252986302523476,
    -0.000240260411712007,
    -0.000222206659492970,
    -0.000198668801151712,
    -0.000169578844691994,
    -0.000134967943726175,
    -0.000094976067777329,
    -0.000049860096743331,
    0.000000000000000000,
    0.000054097216359286,
    0.000111796078442149,
    0.000172333972860101,
    0.000234825428260873,
    0.000298269487006123,
    0.000361560240403592,
    0.000423500531979766,
    0.000482818760273357,
    0.000538188637021932,
    0.000588251680004495,
    0.000631642143880105,
    0.000667014018869279,
    0.000693069657820834,
    0.000708589528831230,
    0.000712462534816516,
    0.000703716294860955,
    0.000681546746228202,
    0.000645346401896314,
    0.000594730587437936,
    0.000529560983848557,
    0.000449965820105035,
    0.000356356091108280,
    0.000249437223225559,
    0.000130215670588441,
    -0.000000000000000001,
    -0.000139603890172795,
    -0.000286703672631030,
    -0.000439137761621857,
    -0.000594498780105894,
    -0.000750163228708207,
    -0.000903327133750850,
    -0.001051047322210335,
    -0.001190287842842693,
    -0.001317970927559997,
    -0.001431031768041246,
    -0.001526476272108699,
    -0.001601440865114015,
    -0.001653253315843600,
    -0.001679493496477621,
    -0.001678052933901441,
    -0.001647191976876998,
    -0.001585593391624306,
    -0.001492411208276258,
    -0.001367313673106573,
    -0.001210519216636156,
    -0.001022824425518419,
    -0.000805623105875338,
    -0.000560915646455428,
    -0.000291308030135310,
    0.000000000000000001,
    0.000309237940764728,
    0.000632098830285042,
    0.000963784790485729,
    0.001299063548595230,
    0.001632335470754199,
    0.001957710436521395,
    0.002269093683046843,
    0.002560279555659481,
    0.002825051921291722,
    0.003057289836130386,
    0.003251076912562411,
    0.003400812706056440,
    0.003501324342964837,
    0.003547976537860242,
    0.003536778106032741,
    0.003464483064800013,
    0.003328684437448438,
    0.003127898926515531,
    0.002861640708769004,
    0.002530482722087065,
    0.002136103963371765,
    0.001681321494935990,
    0.001170106062245550,
    0.000607580455696210,
    -0.000000000000000001,
    -0.000645285176955758,
    -0.001319886162314784,
    -0.002014449339559283,
    -0.002718748014202430,
    -0.003421790770976359,
    -0.004111945460951061,
    -0.004777077438770792,
    -0.005404700407224419,
    -0.005982137983363577,
    -0.006496693881791757,
    -0.006935828420685134,
    -0.007287338898286638,
    -0.007539541265278532,
    -0.007681450434290233,
    -0.007702956523949680,
    -0.007594994332814835,
    -0.007349703379031493,
    -0.006960575924765648,
    -0.006422590529755616,
    -0.005732328844419711,
    -0.004888073557841696,
    -0.003889885656973535,
    -0.002739659427243722,
    -0.001441153927556425,
    0.000000000000000001,
    0.001576317778415438,
    0.003278504433256122,
    0.005095523080383359,
    0.007014688051493388,
    0.009021781774464877,
    0.011101194163548352,
    0.013236082926953814,
    0.015408552872023267,
    0.017599851986273972,
    0.019790581801163755,
    0.021960919309007301,
    0.024090847506079874,
    0.026160391480000506,
    0.028149856849749372,
    0.030040067304191703,
    0.031812597971055817,
    0.033450001383472663,
    0.034936022895171816,
    0.036255802527200516,
    0.037396060406773964,
    0.038345263180017825,
    0.039093769041662216,
    0.039633949322274778,
    0.039960284902866974,
    0.040069436082647777,
    0.039960284902866974,
    0.039633949322274778,
    0.039093769041662216,
    0.038345263180017825,
    0.037396060406773964,
    0.036255802527200516,
    0.034936022895171816,
    0.033450001383472663,
    0.031812597971055824,
    0.030040067304191703,
    0.028149856849749372,
    0.026160391480000510,
    0.024090847506079871,
    0.021960919309007301,
    0.019790581801163758,
    0.017599851986273972,
    0.015408552872023267,
    0.013236082926953815,
    0.011101194163548352,
    0.009021781774464879,
    0.007014688051493388,
    0.005095523080383359,
    0.003278504433256122,
    0.001576317778415438,
    0.000000000000000001,
    -0.001441153927556425,
    -0.002739659427243722,
    -0.003889885656973535,
    -0.004888073557841697,
    -0.005732328844419712,
    -0.006422590529755618,
    -0.006960575924765648,
    -0.007349703379031493,
    -0.007594994332814833,
    -0.007702956523949680,
    -0.007681450434290233,
    -0.007539541265278535,
    -0.007287338898286640,
    -0.006935828420685135,
    -0.006496693881791757,
    -0.005982137983363578,
    -0.005404700407224420,
    -0.004777077438770793,
    -0.004111945460951060,
    -0.003421790770976359,
    -0.002718748014202429,
    -0.002014449339559283,
    -0.001319886162314784,
    -0.000645285176955758,
    -0.000000000000000001,
    0.000607580455696211,
    0.001170106062245550,
    0.001681321494935990,
    0.002136103963371765,
    0.002530482722087065,
    0.002861640708769004,
    0.003127898926515531,
    0.003328684437448440,
    0.003464483064800013,
    0.003536778106032742,
    0.003547976537860242,
    0.003501324342964838,
    0.003400812706056441,
    0.003251076912562411,
    0.003057289836130386,
    0.002825051921291722,
    0.002560279555659481,
    0.002269093683046844,
    0.001957710436521395,
    0.001632335470754199,
    0.001299063548595230,
    0.000963784790485729,
    0.000632098830285043,
    0.000309237940764729,
    0.000000000000000001,
    -0.000291308030135310,
    -0.000560915646455428,
    -0.000805623105875338,
    -0.001022824425518420,
    -0.001210519216636156,
    -0.001367313673106573,
    -0.001492411208276259,
    -0.001585593391624306,
    -0.001647191976876998,
    -0.001678052933901443,
    -0.001679493496477622,
    -0.001653253315843599,
    -0.001601440865114015,
    -0.001526476272108699,
    -0.001431031768041247,
    -0.001317970927559998,
    -0.001190287842842693,
    -0.001051047322210335,
    -0.000903327133750850,
    -0.000750163228708208,
    -0.000594498780105894,
    -0.000439137761621857,
    -0.000286703672631030,
    -0.000139603890172795,
    -0.000000000000000001,
    0.000130215670588441,
    0.000249437223225559,
    0.000356356091108280,
    0.000449965820105035,
    0.000529560983848557,
    0.000594730587437936,
    0.000645346401896314,
    0.000681546746228202,
    0.000703716294860954,
    0.000712462534816517,
    0.000708589528831230,
    0.000693069657820834,
    0.000667014018869279,
    0.000631642143880105,
    0.000588251680004495,
    0.000538188637021933,
    0.000482818760273357,
    0.000423500531979766,
    0.000361560240403592,
    0.000298269487006123,
    0.000234825428260873,
    0.000172333972860101,
    0.000111796078442149,
    0.000054097216359286,
    0.000000000000000000,
    -0.000049860096743331,
    -0.000094976067777329,
    -0.000134967943726175,
    -0.000169578844691994,
    -0.000198668801151712,
    -0.000222206659492970,
    -0.000240260411712007,
    -0.000252986302523476,
    -0.000260617071676855,
    -0.000263449684954200,
    -0.000261832894650648,
    -0.000256154949999037,
    -0.000246831750834351,
    -0.000234295704773931,
    -0.000218985510390934,
    -0.000201337047432889,
    -0.000181775511282446,
    -0.000160708883789383,
    -0.000138522787525481,
    -0.000115576726591127,
    -0.000092201675432196,
    -0.000068698938714455,
    -0.000045340171044719,
    -0.000022368415985591,
    0.000000000000000000,
    0.000021572900859564,
    0.000042179215242215,
    0.000061665650631385,
    0.000079893284958558,
    0.000096734265968441,
]

h3 = [
    -0.000164312671785011,
    -0.000157471139678769,
    -0.000135305540512419,
    -0.000099533312453477,
    -0.000053104835695806,
    0.000000000000000001,
    0.000055063111976598,
    0.000106992446051281,
    0.000150737840924651,
    0.000181731204545302,
    0.000196318445715498,
    0.000192147001444134,
    0.000168471648017458,
    0.000126343326989707,
    0.000068651476987651,
    0.000000000000000000,
    -0.000073589793798068,
    -0.000145139939907779,
    -0.000207313520723995,
    -0.000253105409680910,
    -0.000276567255665093,
    -0.000273497280226764,
    -0.000242020916444558,
    -0.000182991196658120,
    -0.000100148741953726,
    -0.000000000000000001,
    0.000108602144986921,
    0.000215161188465457,
    0.000308477225711349,
    0.000377748370978826,
    0.000413732186932281,
    0.000409849492659528,
    0.000363107727349761,
    0.000274728808855388,
    0.000150387539512510,
    -0.000000000000000001,
    -0.000162955526623413,
    -0.000322553634950152,
    -0.000461891563584317,
    -0.000564786978563534,
    -0.000617541648635894,
    -0.000610588076841197,
    -0.000539833505558148,
    -0.000407533018535886,
    -0.000222560449259940,
    0.000000000000000004,
    0.000239951681215477,
    0.000473710032831008,
    0.000676518741876737,
    0.000824959568636225,
    0.000899511452928619,
    0.000886890938896635,
    0.000781909426538324,
    0.000588614864792190,
    0.000320544827820534,
    -0.000000000000000001,
    -0.000343655296910837,
    -0.000676555172154613,
    -0.000963547316655057,
    -0.001171768071490281,
    -0.001274226078524536,
    -0.001253018389060522,
    -0.001101816342332215,
    -0.000827311253750111,
    -0.000449398915686082,
    0.000000000000000002,
    0.000479449993377002,
    0.000941665851912607,
    0.001338025150626391,
    0.001623512164312170,
    0.001761605806704838,
    0.001728599445878947,
    0.001516867758932288,
    0.001136675455446318,
    0.000616249506338854,
    -0.000000000000000002,
    -0.000655040000762309,
    -0.001284296256798891,
    -0.001821824239789827,
    -0.002206998000889005,
    -0.002391058439438037,
    -0.002342837980641229,
    -0.002053023441640777,
    -0.001536432098028802,
    -0.000831949811357713,
    0.000000000000000002,
    0.000882341860386490,
    0.001728225492628558,
    0.002449307327053706,
    0.002964671546654085,
    0.003209517065463022,
    0.003142711136261822,
    0.002752374902058742,
    0.002058819430716603,
    0.001114381768429957,
    -0.000000000000000003,
    -0.001181312045794768,
    -0.002313606840432023,
    -0.003278986665558062,
    -0.003969424029236265,
    -0.004298273965376276,
    -0.004210300349509614,
    -0.003689122085280967,
    -0.002761183005145843,
    -0.001495647733319344,
    0.000000000000000003,
    0.001588463393136199,
    0.003114629825194378,
    0.004420064556737700,
    0.005358702530731123,
    0.005812248413109875,
    0.005703740189881986,
    0.005007825888900220,
    0.003756544685330773,
    0.002039776649842505,
    -0.000000000000000003,
    -0.002178470082451898,
    -0.004285040016973986,
    -0.006101966190208782,
    -0.007425410247664728,
    -0.008086498743419058,
    -0.007970353898911585,
    -0.007031139352786934,
    -0.005301431512692764,
    -0.002894667347534112,
    0.000000000000000004,
    0.003130433363900129,
    0.006201120042601973,
    0.008898268366842464,
    0.010918421423580290,
    0.011998186362541399,
    0.011942445198344519,
    0.010648408338238494,
    0.008123105172682762,
    0.004492365602501782,
    -0.000000000000000004,
    -0.005003318227276500,
    -0.010081089250661427,
    -0.014740687736742020,
    -0.018469671306137303,
    -0.020775985736004685,
    -0.021228911997830079,
    -0.019497411288476346,
    -0.015382614410572209,
    -0.008841571223070320,
    0.000000000000000004,
    0.010847391800832462,
    0.023249470914877633,
    0.036623546959847986,
    0.050290958368642537,
    0.063520889295581875,
    0.075579221675162248,
    0.085778768190886742,
    0.093527066328890893,
    0.098368058052958715,
    0.100014424748228525,
    0.098368058052958715,
    0.093527066328890893,
    0.085778768190886742,
    0.075579221675162248,
    0.063520889295581875,
    0.050290958368642537,
    0.036623546959847986,
    0.023249470914877633,
    0.010847391800832464,
    0.000000000000000004,
    -0.008841571223070320,
    -0.015382614410572211,
    -0.019497411288476343,
    -0.021228911997830079,
    -0.020775985736004688,
    -0.018469671306137303,
    -0.014740687736742020,
    -0.010081089250661429,
    -0.005003318227276500,
    -0.000000000000000004,
    0.004492365602501783,
    0.008123105172682762,
    0.010648408338238494,
    0.011942445198344519,
    0.011998186362541401,
    0.010918421423580290,
    0.008898268366842464,
    0.006201120042601974,
    0.003130433363900129,
    0.000000000000000004,
    -0.002894667347534112,
    -0.005301431512692764,
    -0.007031139352786934,
    -0.007970353898911585,
    -0.008086498743419058,
    -0.007425410247664728,
    -0.006101966190208784,
    -0.004285040016973988,
    -0.002178470082451899,
    -0.000000000000000003,
    0.002039776649842506,
    0.003756544685330774,
    0.005007825888900221,
    0.005703740189881985,
    0.005812248413109874,
    0.005358702530731122,
    0.004420064556737700,
    0.003114629825194378,
    0.001588463393136199,
    0.000000000000000003,
    -0.001495647733319344,
    -0.002761183005145843,
    -0.003689122085280968,
    -0.004210300349509613,
    -0.004298273965376275,
    -0.003969424029236265,
    -0.003278986665558062,
    -0.002313606840432024,
    -0.001181312045794769,
    -0.000000000000000003,
    0.001114381768429958,
    0.002058819430716603,
    0.002752374902058742,
    0.003142711136261822,
    0.003209517065463022,
    0.002964671546654084,
    0.002449307327053706,
    0.001728225492628559,
    0.000882341860386491,
    0.000000000000000002,
    -0.000831949811357713,
    -0.001536432098028802,
    -0.002053023441640777,
    -0.002342837980641231,
    -0.002391058439438037,
    -0.002206998000889005,
    -0.001821824239789827,
    -0.001284296256798891,
    -0.000655040000762309,
    -0.000000000000000002,
    0.000616249506338854,
    0.001136675455446319,
    0.001516867758932289,
    0.001728599445878947,
    0.001761605806704839,
    0.001623512164312170,
    0.001338025150626391,
    0.000941665851912607,
    0.000479449993377002,
    0.000000000000000002,
    -0.000449398915686083,
    -0.000827311253750111,
    -0.001101816342332215,
    -0.001253018389060522,
    -0.001274226078524538,
    -0.001171768071490281,
    -0.000963547316655057,
    -0.000676555172154613,
    -0.000343655296910837,
    -0.000000000000000001,
    0.000320544827820534,
    0.000588614864792191,
    0.000781909426538325,
    0.000886890938896636,
    0.000899511452928619,
    0.000824959568636226,
    0.000676518741876737,
    0.000473710032831008,
    0.000239951681215477,
    0.000000000000000004,
    -0.000222560449259941,
    -0.000407533018535886,
    -0.000539833505558148,
    -0.000610588076841197,
    -0.000617541648635894,
    -0.000564786978563535,
    -0.000461891563584317,
    -0.000322553634950151,
    -0.000162955526623413,
    -0.000000000000000001,
    0.000150387539512510,
    0.000274728808855388,
    0.000363107727349761,
    0.000409849492659528,
    0.000413732186932281,
    0.000377748370978826,
    0.000308477225711350,
    0.000215161188465457,
    0.000108602144986921,
    -0.000000000000000001,
    -0.000100148741953726,
    -0.000182991196658121,
    -0.000242020916444558,
    -0.000273497280226764,
    -0.000276567255665093,
    -0.000253105409680911,
    -0.000207313520723996,
    -0.000145139939907779,
    -0.000073589793798068,
    0.000000000000000000,
    0.000068651476987651,
    0.000126343326989707,
    0.000168471648017458,
    0.000192147001444135,
    0.000196318445715498,
    0.000181731204545302,
    0.000150737840924651,
    0.000106992446051281,
    0.000055063111976598,
    0.000000000000000001,
    -0.000053104835695806,
    -0.000099533312453477,
    -0.000135305540512419,
    -0.000157471139678769,
    -0.000164312671785011,
]

h4 = [
    0.000000000000000000,
    0.000002974501611384,
    0.000011630961589138,
    0.000022967232209164,
    0.000030716225059778,
    0.000026214839732923,
    0.000000000000000000,
    -0.000055973251773900,
    -0.000145723873974251,
    -0.000266615935880751,
    -0.000407198371448263,
    -0.000546075600414797,
    -0.000652361272314452,
    -0.000688147432914718,
    -0.000613179612975004,
    -0.000391575659878668,
    0.000000000000000001,
    0.000563732118198938,
    0.001273013656973618,
    0.002067373906878073,
    0.002851563067893035,
    0.003500082348355214,
    0.003867862608841334,
    0.003806962971094718,
    0.003188176579066728,
    0.001925429347868523,
    -0.000000000000000002,
    -0.002518961647177852,
    -0.005461249814074702,
    -0.008552964568398333,
    -0.011426676391665728,
    -0.013645225159174835,
    -0.014738246181366184,
    -0.014248680591636921,
    -0.011784851782051391,
    -0.007072431628762949,
    0.000000000000000003,
    0.009347935765629322,
    0.020675604354698812,
    0.033481714360691445,
    0.047087359848541926,
    0.060684558865161380,
    0.073401325498431910,
    0.084376989102916758,
    0.092839977176476990,
    0.098179693861485506,
    0.100004559152954045,
    0.098179693861485506,
    0.092839977176476990,
    0.084376989102916772,
    0.073401325498431910,
    0.060684558865161380,
    0.047087359848541920,
    0.033481714360691452,
    0.020675604354698819,
    0.009347935765629319,
    0.000000000000000003,
    -0.007072431628762950,
    -0.011784851782051391,
    -0.014248680591636925,
    -0.014738246181366184,
    -0.013645225159174839,
    -0.011426676391665735,
    -0.008552964568398330,
    -0.005461249814074704,
    -0.002518961647177853,
    -0.000000000000000002,
    0.001925429347868524,
    0.003188176579066726,
    0.003806962971094720,
    0.003867862608841335,
    0.003500082348355213,
    0.002851563067893038,
    0.002067373906878074,
    0.001273013656973618,
    0.000563732118198938,
    0.000000000000000001,
    -0.000391575659878668,
    -0.000613179612975004,
    -0.000688147432914718,
    -0.000652361272314452,
    -0.000546075600414798,
    -0.000407198371448264,
    -0.000266615935880751,
    -0.000145723873974251,
    -0.000055973251773899,
    0.000000000000000000,
    0.000026214839732923,
    0.000030716225059778,
    0.000022967232209164,
    0.000011630961589138,
    0.000002974501611384,
    0.000000000000000000,
]

def FIR(olist, nlist, start_index, h):
    buffer = []
    for ii in range(len(h)):
        buffer.append(olist[start_index+ii])
    nlist.append(np.average(buffer, weights=h))

def fft(t, data, nt, ndata, dt, title):

    #dt = 1.0/10000.0 # 10kHz
    #t = np.arange(0.0, 1.0, dt) # 10s
    t = np.asarray(t)
    nt = np.asarray(nt)
    # a constant plus 100Hz and 1000Hz
    s = 4.0 * np.sin(2 * np.pi * 100 * t) + 0.25 * np.sin(2 * np.pi * 1000 * t) + 25

    Fs = dt # sample rate
    Ts = 1.0/Fs; # sampling interval
    ts = np.arange(0,t[-1],Ts) # time vector
    y = data # the data to make the fft from
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]

    #for the filtered data
    nts = np.arange(0,nt[-1],Ts) # time vector
    ny = ndata # the data to make the fft from
    nn = len(ny) # length of the signal
    nk = np.arange(nn)
    nT = nn/Fs
    nfrq = k/nT # two sides frequency range
    nfrq = nfrq[range(int(nn/2))] # one side frequency range
    nY = np.fft.fft(ny)/nn # fft computing and normalization
    nY = nY[range(int(nn/2))]

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title(title)
    #ax1.plot(t,y,'b')
    #ax1.set_xlabel('Time')
    #ax1.set_ylabel('Amplitude')
    ax1.plot(t, data, 'black')
    ax1.plot(nt, ndata, 'red') #filtered
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Signal')
    ax2.loglog(frq,abs(Y),'black') # plotting the fft
    ax2.loglog(nfrq,abs(nY),'red') # plotting the filtered fft
    ax2.set_xlabel('Freq (Hz)')
    ax2.set_ylabel('|Y(freq)|')
    #plt.show()

t1 = []
t2 = []
t3 = []
t4 = []
data1 = [] # sigA
data2 = [] # sigB
data3 = [] # sigC
data4 = [] # sigD

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t1.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
dt1 = len(t1)/t1[-1]
ndata1 = []
for ii in range(len(data1)-len(h1)):
    FIR(data1, ndata1, ii, h1)
print("Sample rate 1: " + str(dt1))
nt1 = t1[:len(data1)-len(h1)]
fft(t1, data1, nt1, ndata1, dt1, title1)


with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t2.append(float(row[0])) # leftmost column
        data2.append(float(row[1])) # second column
dt2 = len(t2)/t2[-1]
ndata2 = []
for ii in range(len(data2)-len(h2)):
    FIR(data2, ndata2, ii, h2)
print("Sample rate 2: " + str(dt2))
nt2 = t2[:len(data2)-len(h2)]
fft(t2, data2, nt2, ndata2, dt2, title2)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t3.append(float(row[0])) # leftmost column
        data3.append(float(row[1])) # second column
dt3 = len(t3)/t3[-1]
ndata3 = []
for ii in range(len(data3)-len(h3)):
    FIR(data3, ndata3, ii, h3)
print("Sample rate 3: " + str(dt3))
nt3 = t3[:len(data3)-len(h3)]
fft(t3, data3, nt3, ndata3, dt3, title3)

with open('D:/Northwestern/ME433/MECH_ENG_433_Yen/HW2/sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t4.append(float(row[0])) # leftmost column
        data4.append(float(row[1])) # second column
dt4 = len(t4)/t4[-1]
ndata4 = []
for ii in range(len(data4)-len(h4)):
    FIR(data4, ndata4, ii, h4)
print("Sample rate 4: " + str(dt4))
nt4 = t4[:len(data4)-len(h4)]
#ndata4.reverse()
fft(t4, data4, nt4, ndata4, dt4, title4)

plt.show()