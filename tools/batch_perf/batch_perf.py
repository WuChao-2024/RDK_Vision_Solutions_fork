import os
import argparse
import subprocess



RED_BEGIN = ""
GREEN_BEGIN = ""
COLOR_END = ""

def main():
    # 参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default="", help='Path to Load Test Image.')
    parser.add_argument('--max', type=int, default=2, help='Classes Num to Detect.')
    opt = parser.parse_args()
    # 输出perf信息
    opt.file = os.path.join(os.getcwd(), opt.file)
    print("Perf file: %s"%opt.file)
    print("Max Thread_num: %d"%opt.max)
    
    # 检查是否有 hrt_model_exec 命令
    result = subprocess.run("hrt_model_exec", shell=True, capture_output=True, text=True).stdout
    if "command not found" in result:
        print("hrt_model_exec not found.")
        exit(-1)
    print("hrt_model_exec found, continue.")

    # 检查目标目录是否存在
    if not os.path.exists(opt.file):
        print("File not found.")
        exit(-1)

    # 获取当前的目标目录文件
    file_names = os.listdir(opt.file)

    # 获取所有*.bin文件对应的文件大小，并排序
    bin_file_num = 0
    for file_name in file_names:
        if file_name 

    # 输出hrut_somstatus的信息
    print("hrut_somstatus")

    # 输出所有*.bin文件的名称和大小

    # 开始逐个perf

    ## 输出perf进度
    ## 输出CPU温度
   # /sys/class/hwmon/hwmon0
    

    ## 输出perf的耗时和总耗时

    ## 输出perf结果
    pass



def get_perf_data(model_file, thread_num):
    cmd = "hrt_model_exec perf --model_file %s --thread_num %s"%(model_file, thread_num)
    msg = os.system(cmd)

if __name__ == "__main__":
    main()
