import matplotlib.pyplot as plt
import numpy as np
# time is in nanoseconds

def get_results(time_dict:dict, calls_dict:dict):
    result_dict = {}
    for func, calls in calls_dict.items():
        # print(func, calls, time_dict[func])
        if calls != 0:
            result_dict[func] = time_dict[func] / calls
        else:
            result_dict[func] = 0
    return result_dict


def finalize_logs(logs: list):
    r1, r2, r3 = logs[0], logs[1], logs[2]
    final = {}
    for func, avg_time in r1.items():
        final[func] = ( (avg_time + r2[func] + r3[func]) / 3 ) / 10 ** 6
    return final


def get_avgs(logs: list):
    results = []
    for i in range(0, len(logs) - 1, 2):
        calls = logs[i]
        times = logs[i+1]
        results.append(get_results(times, calls))
    return finalize_logs(results)


def print_avgs(final: dict):
    funcFinal = ""
    strFinal = ""
    for func, avg_time in final.items():
        funcFinal += func + ", "
        strFinal += str(avg_time) + ", "
    print(funcFinal)
    print(strFinal)


# 0 conflicts, thrify = true, cb= 10
# CALLS_TH_TRUE_C_0_CB_10_R_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":15682,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_TRUE_C_0_CB_10_R_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":524366190,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_TRUE_C_0_CB_10_R_1 = {"handleAccept":7,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":15021,"handlePreAccept":15023,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_TRUE_C_0_CB_10_R_1 = {"handleAccept":54183,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":25172211,"handlePreAccept":1192952325,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_TRUE_C_0_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":7,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":8096,"handlePreAcceptReply":6709,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14806,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_TRUE_C_0_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":5481936,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":38619004623,"handlePreAcceptReply":7851370964,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":7637246220,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
#
# # PLOT SETTINGS
#
#
# logs = [CALLS_TH_TRUE_C_0_CB_10_R_2, TIMES_TH_TRUE_C_0_CB_10_R_2, CALLS_TH_TRUE_C_0_CB_10_R_1, TIMES_TH_TRUE_C_0_CB_10_R_1, CALLS_TH_TRUE_C_0_CB_10_R_0, TIMES_TH_TRUE_C_0_CB_10_R_0]
# print("CONFLICTS = 0, THRIFTY = TRUE, CB = 10: ")
# TH_TRUE_C_0_CB_10_RESULT = get_avgs(logs)
# print_avgs(TH_TRUE_C_0_CB_10_RESULT)
#
# # 100 conflicts, thrify = true, cb = 10
# CALLS_TH_TRUE_C_100_CB_10_R_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":15993,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_TRUE_C_100_CB_10_R_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":373602202,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_TRUE_C_100_CB_10_R_1 = {"handleAccept":7,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":15190,"handlePreAccept":15191,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_TRUE_C_100_CB_10_R_1 = {"handleAccept":79372,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":24722145,"handlePreAccept":878666341,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_TRUE_C_100_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":7,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":7750,"handlePreAcceptReply":7217,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14968,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_TRUE_C_100_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":9664063,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":37248962963,"handlePreAcceptReply":9054644986,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":7422957372,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
#
# logs = [CALLS_TH_TRUE_C_100_CB_10_R_2, TIMES_TH_TRUE_C_100_CB_10_R_2, CALLS_TH_TRUE_C_100_CB_10_R_1, TIMES_TH_TRUE_C_100_CB_10_R_1, CALLS_TH_TRUE_C_100_CB_10_R_0, TIMES_TH_TRUE_C_100_CB_10_R_0]
# print("CONFLICTS = 100, THRIFTY = TRUE, CB = 10: ")
# TH_TRUE_C_100_CB_10_RESULT = get_avgs(logs)
# print_avgs(TH_TRUE_C_100_CB_10_RESULT)
#
#
# CALLS_TH_FALSE_C_0_CB_10_R_2 = {"handleAccept":3,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22315,"handlePreAccept":22318,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_FALSE_C_0_CB_10_R_2 = {"handleAccept":18621,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":19931839,"handlePreAccept":1347973538,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_FALSE_C_0_CB_10_R_1 = {"handleAccept":3,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22293,"handlePreAccept":22295,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_FALSE_C_0_CB_10_R_1 = {"handleAccept":18552,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":19960197,"handlePreAccept":1402914382,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_FALSE_C_0_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":6,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":12628,"handlePreAcceptReply":31663,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":22151,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_FALSE_C_0_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":336150,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":22142555321,"handlePreAcceptReply":16515921133,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":13502868606,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
#
# logs = [CALLS_TH_FALSE_C_0_CB_10_R_2, TIMES_TH_FALSE_C_0_CB_10_R_2, CALLS_TH_FALSE_C_0_CB_10_R_1, TIMES_TH_FALSE_C_0_CB_10_R_1, CALLS_TH_FALSE_C_0_CB_10_R_0, TIMES_TH_FALSE_C_0_CB_10_R_0]
# print("CONFLICTS = 0, THRIFTY = FALSE, CB = 10: ")
# TH_FALSE_C_0_CB_10_RESULT = get_avgs(logs)
# print_avgs(TH_FALSE_C_0_CB_10_RESULT)
#
#
# CALLS_TH_FALSE_C_100_CB_10_R_2 = {"handleAccept":4,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22463,"handlePreAccept":22465,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_FALSE_C_100_CB_10_R_2 = {"handleAccept":27703,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":21939953,"handlePreAccept":1054308043,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_FALSE_C_100_CB_10_R_1 = {"handleAccept":4,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22471,"handlePreAccept":22472,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_FALSE_C_100_CB_10_R_1 = {"handleAccept":34978,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":20135522,"handlePreAccept":1061656667,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CALLS_TH_FALSE_C_100_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":8,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":12533,"handlePreAcceptReply":31773,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":22156,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# TIMES_TH_FALSE_C_100_CB_10_R_0 = {"handleAccept":0,"handleAcceptReply":2386185,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":22185910949,"handlePreAcceptReply":17019976105,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":12396058104,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# logs = [CALLS_TH_FALSE_C_100_CB_10_R_2, TIMES_TH_FALSE_C_100_CB_10_R_2, CALLS_TH_FALSE_C_100_CB_10_R_1, TIMES_TH_FALSE_C_100_CB_10_R_1, CALLS_TH_FALSE_C_100_CB_10_R_0, TIMES_TH_FALSE_C_100_CB_10_R_0]
# print("CONFLICTS = 100, THRIFTY = FALSE, CB = 10: ")
# TH_FALSE_C_100_CB_10_RESULT = get_avgs(logs)
# print_avgs(TH_FALSE_C_100_CB_10_RESULT)
#
# # plot settings
#
# LABELS = TH_FALSE_C_100_CB_10_RESULT.keys()  # can be any
# THRIFTY_ON_C_0_GRAPH = TH_TRUE_C_0_CB_10_RESULT.values()
# THRIFTY_ON_C_100_GRAPH = TH_TRUE_C_100_CB_10_RESULT.values()
#
# x = np.arange(len(LABELS))  # the label locations
# width = 0.35  # the width of the bars
#
# fig, ax = plt.subplots()
#
# rects1 = ax.bar(x - width/2, THRIFTY_ON_C_0_GRAPH, width, label='Conflicts = 0')
# rects2 = ax.bar(x + width/2, THRIFTY_ON_C_100_GRAPH, width, label='Conflicts = 100')
#
# ax.set_ylabel('Avg Time (ms)')
# ax.set_title('Avg Time by Conflict Grouping, Thrifty ON')
#
# ax.set_xticks(x)
# ax.set_xticklabels(LABELS, rotation=90)
# plt.ylim(top=1.8)
#
# ax.legend()
# # ax.bar_label(rects1, padding=3)
# # ax.bar_label(rects2, padding=3)
#
# fig.tight_layout(pad=3.0)
#
# plt.savefig("epaxos_thrifty_on_conflicts.png")
# # plt.show()
#
#
# LABELS = TH_FALSE_C_100_CB_10_RESULT.keys()  # can be any
# THRIFTY_OFF_C_0_GRAPH = TH_FALSE_C_0_CB_10_RESULT.values()
# THRIFTY_OFF_C_100_GRAPH = TH_FALSE_C_100_CB_10_RESULT.values()
#
# x = np.arange(len(LABELS))  # the label locations
# width = 0.35  # the width of the bars
#
# fig2, ax = plt.subplots()
#
# rects1 = ax.bar(x - width/2, THRIFTY_OFF_C_0_GRAPH, width, label='Conflicts = 0')
# rects2 = ax.bar(x + width/2, THRIFTY_OFF_C_100_GRAPH, width, label='Conflicts = 100')
#
# ax.set_ylabel('Avg Time (ms)')
# ax.set_title('Avg Time by Conflict Grouping, Thrifty OFF')
#
# ax.set_xticks(x)
# ax.set_xticklabels(LABELS, rotation=90)
# plt.ylim(top=0.9)
#
#
# ax.legend()
# # ax.bar_label(rects1, padding=3)
# # ax.bar_label(rects2, padding=3)
#
# fig2.tight_layout(pad=3.0)
#
# plt.savefig("epaxos_thrifty_off_conflicts.png")
# # plt.show()



# 0 conflicts, thrify = true
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":7,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":8096,"handlePreAcceptReply":6709,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14806,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:5.481936ms handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:38.619004623s handlePreAcceptReply:7.851370964s handlePrepare:0s handlePrepareReply:0s handlePropose:7.63724622s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":5481936,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":38619004623,"handlePreAcceptReply":7851370964,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":7637246220,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":7,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":15021,"handlePreAccept":15023,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:54.183µs handleAcceptReply:0s handleCommit:0s handleCommitShort:25.172211ms handlePreAccept:1.192952325s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":54183,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":25172211,"handlePreAccept":1192952325,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  2
# Call Dict:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":15682,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:0s handleCommit:524.36619ms handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":524366190,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

# 100 conflicts, thrifty = true
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":7,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":7750,"handlePreAcceptReply":7217,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14968,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:9.664063ms handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:37.248962963s handlePreAcceptReply:9.054644986s handlePrepare:0s handlePrepareReply:0s handlePropose:7.422957372s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":9664063,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":37248962963,"handlePreAcceptReply":9054644986,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":7422957372,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":7,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":15190,"handlePreAccept":15191,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:79.372µs handleAcceptReply:0s handleCommit:0s handleCommitShort:24.722145ms handlePreAccept:878.666341ms handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":79372,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":24722145,"handlePreAccept":878666341,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  2
# Call Dict:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":15993,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:0s handleCommit:373.602202ms handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":373602202,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

# 0 conflicts, thrifty = false
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":6,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":12628,"handlePreAcceptReply":31663,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":22151,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:336.15µs handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:22.142555321s handlePreAcceptReply:16.515921133s handlePrepare:0s handlePrepareReply:0s handlePropose:13.502868606s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":336150,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":22142555321,"handlePreAcceptReply":16515921133,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":13502868606,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":3,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22293,"handlePreAccept":22295,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:18.552µs handleAcceptReply:0s handleCommit:0s handleCommitShort:19.960197ms handlePreAccept:1.402914382s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":18552,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":19960197,"handlePreAccept":1402914382,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  2
# Call Dict:  {"handleAccept":3,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22315,"handlePreAccept":22318,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:18.621µs handleAcceptReply:0s handleCommit:0s handleCommitShort:19.931839ms handlePreAccept:1.347973538s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":18621,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":19931839,"handlePreAccept":1347973538,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}


# 100 conflicts, thrifty = false
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":8,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":12533,"handlePreAcceptReply":31773,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":22156,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:2.386185ms handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:22.185910949s handlePreAcceptReply:17.019976105s handlePrepare:0s handlePrepareReply:0s handlePropose:12.396058104s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":2386185,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":22185910949,"handlePreAcceptReply":17019976105,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":12396058104,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  2
# Call Dict:  {"handleAccept":4,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22463,"handlePreAccept":22465,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:27.703µs handleAcceptReply:0s handleCommit:0s handleCommitShort:21.939953ms handlePreAccept:1.054308043s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":27703,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":21939953,"handlePreAccept":1054308043,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":4,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22471,"handlePreAccept":22472,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:34.978µs handleAcceptReply:0s handleCommit:0s handleCommitShort:20.135522ms handlePreAccept:1.061656667s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":34978,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":20135522,"handlePreAccept":1061656667,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}



######################################################################################################



# Batching Tests

# Batch = 1
# Replica:  1
# Call Dict:  {"handleAccept":34,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":169674,"handlePreAccept":169675,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:368.616µs handleAcceptReply:0s handleCommit:0s handleCommitShort:140.732909ms handlePreAccept:3.205819824s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":368616,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":140732909,"handlePreAccept":3205819824,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":68,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":249994,"handlePreAcceptReply":89289,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":169738,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:7.962217ms handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:1m24.60794808s handlePreAcceptReply:15.06710892s handlePrepare:0s handlePrepareReply:0s handlePropose:30.35560328s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":7962217,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":84607948080,"handlePreAcceptReply":15067108920,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":30355603280,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  2
# Call Dict:  {"handleAccept":34,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":169905,"handlePreAccept":169905,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:273.663µs handleAcceptReply:0s handleCommit:0s handleCommitShort:119.698961ms handlePreAccept:3.14652302s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":273663,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":119698961,"handlePreAccept":3146523020,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

CB_1_CALL_R1 = {"handleAccept":34,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":169674,"handlePreAccept":169675,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_TIME_R1 = {"handleAccept":368616,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":140732909,"handlePreAccept":3205819824,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CALL_R0 = {"handleAccept":0,"handleAcceptReply":68,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":249994,"handlePreAcceptReply":89289,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":169738,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_TIME_R0 = {"handleAccept":0,"handleAcceptReply":7962217,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":84607948080,"handlePreAcceptReply":15067108920,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":30355603280,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CALL_R2 = {"handleAccept":34,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":169905,"handlePreAccept":169905,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_TIME_R2 = {"handleAccept":273663,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":119698961,"handlePreAccept":3146523020,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

print("Client Batch = 1")
CB_1_RESULT = get_avgs([CB_1_CALL_R1, CB_1_TIME_R1, CB_1_CALL_R0, CB_1_TIME_R0, CB_1_CALL_R2, CB_1_TIME_R2])
print_avgs(CB_1_RESULT)

CB_10_CALL_R1 = {"handleAccept":35,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":23763,"handlePreAccept":23763,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_10_TIME_R1 = {"handleAccept":354926,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22743373,"handlePreAccept":1502289556,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_10_CALL_R0 = {"handleAccept":0,"handleAcceptReply":70,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":13308,"handlePreAcceptReply":34214,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":23763,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_10_TIME_R0 = {"handleAccept":0,"handleAcceptReply":23814066,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":22914272209,"handlePreAcceptReply":19381186832,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14240012584,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_10_CALL_R2 = {"handleAccept":35,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":23763,"handlePreAccept":23763,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_10_TIME_R2 = {"handleAccept":267054,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":20696551,"handlePreAccept":1392879348,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}


# Replica:  2
# Call Dict:  {"handleAccept":35,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":23763,"handlePreAccept":23763,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:267.054µs handleAcceptReply:0s handleCommit:0s handleCommitShort:20.696551ms handlePreAccept:1.392879348s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":267054,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":20696551,"handlePreAccept":1392879348,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":35,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":23763,"handlePreAccept":23763,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:354.926µs handleAcceptReply:0s handleCommit:0s handleCommitShort:22.743373ms handlePreAccept:1.502289556s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":354926,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":22743373,"handlePreAccept":1502289556,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":70,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":13308,"handlePreAcceptReply":34214,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":23763,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:23.814066ms handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:22.914272209s handlePreAcceptReply:19.381186832s handlePrepare:0s handlePrepareReply:0s handlePropose:14.240012584s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":23814066,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":22914272209,"handlePreAcceptReply":19381186832,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14240012584,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

print("Client Batch = 10")
CB_10_RESULT = get_avgs([CB_10_CALL_R1, CB_10_TIME_R1, CB_10_CALL_R0, CB_10_TIME_R0, CB_10_CALL_R2, CB_10_TIME_R2])
print_avgs(CB_10_RESULT)


CB_20_CALL_R1 = {"handleAccept":73,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":12382,"handlePreAccept":12382,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_20_TIME_R1 = {"handleAccept":818865,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":14934990,"handlePreAccept":1362012662,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_20_CALL_R0 = {"handleAccept":0,"handleAcceptReply":146,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":6755,"handlePreAcceptReply":18009,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":12382,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_20_TIME_R0 = {"handleAccept":0,"handleAcceptReply":154147319,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":11144767720,"handlePreAcceptReply":22816107195,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":13559472620,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_20_CALL_R2 = {"handleAccept":73,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":12382,"handlePreAccept":12382,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_20_TIME_R2 = {"handleAccept":412306,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":15088525,"handlePreAccept":1325033769,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":146,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":6755,"handlePreAcceptReply":18009,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":12382,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:154.147319ms handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:11.14476772s handlePreAcceptReply:22.816107195s handlePrepare:0s handlePrepareReply:0s handlePropose:13.55947262s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":154147319,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":11144767720,"handlePreAcceptReply":22816107195,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":13559472620,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  2
# Call Dict:  {"handleAccept":73,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":12382,"handlePreAccept":12382,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:412.306µs handleAcceptReply:0s handleCommit:0s handleCommitShort:15.088525ms handlePreAccept:1.325033769s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":412306,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":15088525,"handlePreAccept":1325033769,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":73,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":12382,"handlePreAccept":12382,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:818.865µs handleAcceptReply:0s handleCommit:0s handleCommitShort:14.93499ms handlePreAccept:1.362012662s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":818865,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":14934990,"handlePreAccept":1362012662,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

print("Client Batch = 20")
CB_20_RESULT = get_avgs([CB_20_CALL_R1, CB_20_TIME_R1, CB_20_CALL_R0, CB_20_TIME_R0, CB_20_CALL_R2, CB_20_TIME_R2])
print_avgs(CB_20_RESULT)



CB_40_CALL_R1 = {"handleAccept":327,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10756,"handlePreAccept":10756,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_40_TIME_R1 = {"handleAccept":3354583,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":13172091,"handlePreAccept":1346111132,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_40_CALL_R0 = {"handleAccept":0,"handleAcceptReply":654,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3929,"handlePreAcceptReply":17583,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":10756,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_40_TIME_R0 = {"handleAccept":0,"handleAcceptReply":1067464670,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":6453206466,"handlePreAcceptReply":25969835938,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14056997658,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_40_CALL_R2 = {"handleAccept":327,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10756,"handlePreAccept":10756,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_40_TIME_R2 = {"handleAccept":2650662,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":13129691,"handlePreAccept":1317336363,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}


#
# Replica:  2
# Call Dict:  {"handleAccept":327,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10756,"handlePreAccept":10756,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:2.650662ms handleAcceptReply:0s handleCommit:0s handleCommitShort:13.129691ms handlePreAccept:1.317336363s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":2650662,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":13129691,"handlePreAccept":1317336363,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":327,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10756,"handlePreAccept":10756,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:3.354583ms handleAcceptReply:0s handleCommit:0s handleCommitShort:13.172091ms handlePreAccept:1.346111132s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":3354583,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":13172091,"handlePreAccept":1346111132,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":654,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3929,"handlePreAcceptReply":17583,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":10756,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:1.06746467s handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:6.453206466s handlePreAcceptReply:25.969835938s handlePrepare:0s handlePrepareReply:0s handlePropose:14.056997658s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":1067464670,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":6453206466,"handlePreAcceptReply":25969835938,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":14056997658,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}


print("Client Batch = 40")
CB_40_RESULT = get_avgs([CB_40_CALL_R1, CB_40_TIME_R1, CB_40_CALL_R0, CB_40_TIME_R0, CB_40_CALL_R2, CB_40_TIME_R2])
print_avgs(CB_40_RESULT)



CB_80_CALL_R1 = {"handleAccept":529,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10208,"handlePreAccept":10208,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_80_TIME_R1 = {"handleAccept":5251172,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":11649944,"handlePreAccept":1385547071,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_80_CALL_R0 = {"handleAccept":0,"handleAcceptReply":1058,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3122,"handlePreAcceptReply":17294,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":10208,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_80_TIME_R0 = {"handleAccept":0,"handleAcceptReply":1342276108,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":4153507341,"handlePreAcceptReply":21655302078,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":12723884896,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_80_CALL_R2 = {"handleAccept":529,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10208,"handlePreAccept":10208,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_80_TIME_R2 = {"handleAccept":4429238,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":13530037,"handlePreAccept":1402756546,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}



# Replica:  2
# Call Dict:  {"handleAccept":529,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10208,"handlePreAccept":10208,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:4.429238ms handleAcceptReply:0s handleCommit:0s handleCommitShort:13.530037ms handlePreAccept:1.402756546s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":4429238,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":13530037,"handlePreAccept":1402756546,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":529,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":10208,"handlePreAccept":10208,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:5.251172ms handleAcceptReply:0s handleCommit:0s handleCommitShort:11.649944ms handlePreAccept:1.385547071s handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":5251172,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":11649944,"handlePreAccept":1385547071,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":1058,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3122,"handlePreAcceptReply":17294,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":10208,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:1.342276108s handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:4.153507341s handlePreAcceptReply:21.655302078s handlePrepare:0s handlePrepareReply:0s handlePropose:12.723884896s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":1342276108,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":4153507341,"handlePreAcceptReply":21655302078,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":12723884896,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}


print("Client Batch = 80")
CB_80_RESULT = get_avgs([CB_80_CALL_R1, CB_80_TIME_R1, CB_80_CALL_R0, CB_80_TIME_R0, CB_80_CALL_R2, CB_80_TIME_R2])
print_avgs(CB_80_RESULT)


CB_1_CLIENTS_1_CALL_R1 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1899,"handlePreAccept":1899,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CLIENTS_1_TIME_R1 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1378745,"handlePreAccept":30078121,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CLIENTS_1_CALL_R0 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3875,"handlePreAcceptReply":19,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":1983,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CLIENTS_1_TIME_R0 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":86351104,"handlePreAcceptReply":12414,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":68166028,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CLIENTS_1_CALL_R2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1892,"handlePreAccept":1893,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
CB_1_CLIENTS_1_TIME_R2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1308822,"handlePreAccept":31698838,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

print("Client Batch = 1")
CB_1_CLIENTS_1_RESULT = get_avgs([CB_1_CLIENTS_1_CALL_R1, CB_1_CLIENTS_1_TIME_R1, CB_1_CLIENTS_1_CALL_R0, CB_1_CLIENTS_1_TIME_R0, CB_1_CLIENTS_1_CALL_R2, CB_1_CLIENTS_1_TIME_R2])
print_avgs(CB_1_CLIENTS_1_RESULT)

# Replica:  2
# Call Dict:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1892,"handlePreAccept":1893,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:0s handleCommit:0s handleCommitShort:1.308822ms handlePreAccept:31.698838ms handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1308822,"handlePreAccept":31698838,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Replica:  1
# Call Dict:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1899,"handlePreAccept":1899,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:0s handleCommit:0s handleCommitShort:1.378745ms handlePreAccept:30.078121ms handlePreAcceptOK:0s handlePreAcceptReply:0s handlePrepare:0s handlePrepareReply:0s handlePropose:0s handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1378745,"handlePreAccept":30078121,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# pid: 9861, cmd: /root/go/src/epaxos/bin/server -port 17070 -maddr 10.142.0.27 -addr 10.142.0.27 -p 4 -thrifty=false -e=true
# pid: 9385, cmd: /root/go/src/epaxos/bin/server -port 17072 -maddr 10.142.0.27 -addr 10.142.0.63 -p 4 -thrifty=false -e=true
# Replica:  0
# Call Dict:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3875,"handlePreAcceptReply":19,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":1983,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# Time Dict Map:  map[handleAccept:0s handleAcceptReply:0s handleCommit:0s handleCommitShort:0s handlePreAccept:0s handlePreAcceptOK:86.351104ms handlePreAcceptReply:12.414µs handlePrepare:0s handlePrepareReply:0s handlePropose:68.166028ms handleTryPreAccept:0s handleTryPreAcceptReply:0s]
# Time Dict UnMarshalled:  {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":86351104,"handlePreAcceptReply":12414,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":68166028,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}

#
# # Replica:  2
# CB_1_CLIENTS_1_CALL_R2_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1366,"handlePreAccept":1366,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CB_1_CLIENTS_1_TIME_R2_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1096661,"handlePreAccept":21125849,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# # Replica:  1
# CB_1_CLIENTS_1_CALL_R1_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1421,"handlePreAccept":1422,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CB_1_CLIENTS_1_TIME_R1_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":1388554,"handlePreAccept":29187634,"handlePreAcceptOK":0,"handlePreAcceptReply":0,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":0,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# # Replica:  0
# CB_1_CLIENTS_1_CALL_R0_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":3072,"handlePreAcceptReply":34,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":1558,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# CB_1_CLIENTS_1_TIME_R0_2 = {"handleAccept":0,"handleAcceptReply":0,"handleCommit":0,"handleCommitShort":0,"handlePreAccept":0,"handlePreAcceptOK":50337875,"handlePreAcceptReply":138545,"handlePrepare":0,"handlePrepareReply":0,"handlePropose":50759193,"handleTryPreAccept":0,"handleTryPreAcceptReply":0}
# print("Client Batch = 1 Rd 2")
# CB_1_CLIENTS_1_RESULT_2 = get_avgs([CB_1_CLIENTS_1_CALL_R1_2, CB_1_CLIENTS_1_TIME_R1_2, CB_1_CLIENTS_1_CALL_R0_2, CB_1_CLIENTS_1_TIME_R0_2, CB_1_CLIENTS_1_CALL_R2_2, CB_1_CLIENTS_1_TIME_R2_2])
# print_avgs(CB_1_CLIENTS_1_RESULT_2)

LABELS = CB_1_CALL_R0.keys()  # can be any

x = np.arange(len(LABELS))  # the label locations
width = 0.05  # the width of the bars

fig2, ax = plt.subplots()

SPACE_FACTOR = 0.2

rects1 = ax.bar(x + SPACE_FACTOR - width, CB_1_RESULT.values(), width, label='ClientBatch = 1')
rects2 = ax.bar(x + SPACE_FACTOR - 2 * width, CB_10_RESULT.values(), width, label='ClientBatch = 10')
rects3 = ax.bar(x + SPACE_FACTOR - 3 * width, CB_20_RESULT.values(), width, label='ClientBatch = 20')
rects4 = ax.bar(x + SPACE_FACTOR - 4 * width, CB_40_RESULT.values(), width, label='ClientBatch = 40')
rects5 = ax.bar(x + SPACE_FACTOR - 5 * width, CB_80_RESULT.values(), width, label='ClientBatch = 80')
rects6 = ax.bar(x + SPACE_FACTOR - 6 * width, CB_1_CLIENTS_1_RESULT.values(), width, label='ClientBatch = 1, NClients = 1')

ax.set_ylabel('Avg Runtime (ms)')
ax.set_title('Avg Runtime by Client Batch, Optimal Situation')

ax.set_xticks(x)
ax.set_xticklabels(LABELS, rotation=90)
plt.ylim(top=0.9)


ax.legend()
# ax.bar_label(rects1, padding=3)
# ax.bar_label(rects2, padding=3)

fig2.tight_layout(pad=3.0)

# plt.savefig("epaxos_thrifty_off_conflicts_0_client_batch.png")
plt.show()


