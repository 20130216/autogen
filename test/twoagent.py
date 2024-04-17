from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample

# 原来的代码
# config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
# user_proxy = UserProxyAgent(
#     "user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}
# )  # IMPORTANT: set to True to run code in docker, recommended
# user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")


config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST.json",
    file_location="/Users/wingzheng/Desktop/github/autogen",
    # file_location="/autogen",     ## "use_docker": True时 用这个时反而不对  ？？
    filter_dict={
        "model": {
            "gpt-3.5-turbo",
            # "gpt-4",
            # "gpt4",
            # "gpt-4-turbo",
            # "gpt-3.5-turbo-0301",
            # "chatgpt-35-turbo-0301",
            # "gpt-35-turbo-v0301",
            # "gpt",
        }
    }
)
print("config_list: "+str(config_list))

assistant = AssistantAgent("assistant", llm_config={
                           "config_list": config_list})

user_proxy = UserProxyAgent(
    # ,"container_id":"7313e0c840f02c4aef307bfd5d2895ff88914c651bdb5905d5d14ec418d33885"  }   ##"keep_container": True ##"container_name":"autogen_base_container"
    "user_proxy", code_execution_config={"work_dir": "coding", "use_docker": "python:3.10.13"}
    # "user_proxy", code_execution_config={"work_dir": "coding", "use_docker":"autogen_base_img"}   ##hello-world:latest    ##"yuandongtian/autogen:latest"
)  # IMPORTANT: set to True to run code in docker, recommended  "python:3.10.13"    "python:3-slim"  "yuandongtian/autogen:latest" "jeefy/autogen-studio:latest"
   #pip install yfinance pandas  matplotlib  diskcache  plotly

print("use_docker is: "+str(user_proxy.use_docker)+"\n" +
      "user_proxy._code_execution_config: "+str(user_proxy._code_execution_config))
# 打印Python解释器的路径;docker中运行显示如/usr/bin/python3
print("sys.executable: "+sys.executable)
# print("sys.path: "+str(sys.path)) ##打印模块搜索路径
# print("HOSTNAME: "+os.environ['HOSTNAME'])
# 如果您的代码是在一个Docker容器中运行的，那么os.environ[‘HOSTNAME’]会返回一个类似于
print("HOSTNAME: "+os.environ.get('HOSTNAME', 'unknown'))
# e9f6c3f8d7f4的字符串，这是一个随机生成的哈希值，用于标识容器。如果您的代码是在您的主机系统中运行的，那么os.environ[‘HOSTNAME’]会返回您的主机系统的主机名，
# 例如DESKTOP-123456
print("DOCKER_IMAGE: "+os.environ.get('DOCKER_IMAGE', 'unknown'))
# 如果您的代码是在一个Docker容器中运行的，那么socket.gethostname()会返回容器的主机名。容器的主机名默认是
print("socket HOSTNAME: "+socket.gethostname())
# 一个随机生成的哈希值，例如e9f6c3f8d7f4
# 如果您的代码是在您的主机系统中运行的，那么socket.gethostname()会返回您的主机系统的主机名 例如DESKTOP-123456。
# 如果返回值与您的主机系统的主机名不一致，那么说明Docker已经启动了，并且您的代码正在一个Docker容器中运行。如果返回值与您的主机系统的主机名一致，那么说明
# Docker没有启动，或者您的代码没有在一个Docker容器中运行


# user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD in the last year")
# user_proxy.initiate_chat(assistant, message="Plot a chart of alibaba stock price change YTD in the last year.")
# user_proxy.initiate_chat(assistant, message="Plot a chart of Moutai stock price change YTD in the last 2 year.")

user_proxy.initiate_chat(assistant, message="最近这段时间中国发生了股灾，很多股民哀鸿遍野，请以股灾为题，写一首打油诗.表达股民无奈的心情")
# user_proxy.initiate_chat(assistant, message="中国国家总理李克强病逝，请为他写一首悼亡诗")
