---------------------AI integration with local Qwen LLMs and Autopsy 4.23.0----------------

The Autopsy Model Context Protocol (MCP) interface, introduced in Autopsy 4.23.0, provides a read-only interface for querying and summarising open forensic cases using AI clients like Claude Desktop, Claude Code, or local LLM tools such as LM Studio.

To keep AI queries local and private, we will use LM Studio and the Qwen3.5-4b LLM (and Autopsy), in the following two scenarios.

Scenario 1. Use LM Studio to query tools in Autopsy
---------------------------------------------------


https://lmstudio.ai/download/latest/win32/x64

https://lmstudio.ai/models/qwen/qwen3.5-4b

It is necessary to restrict or filter the number of Autopsy Tools that LM Studio sees, when you don't have access to GPU cores. This is done by wrapping a python script, in the mcp json configuration in LM Studio. By restricting LM Studio to the get_server_status and get_data_artifacts, you can comfortably query browser access/downloads. I used an EC2 compute r5.large (16GB). The default model context size is to small (8192), so increase it to 52768. We will treat Web browsing in ine prompt/context.

<img width="523" height="118" alt="Picture1" src="https://github.com/user-attachments/assets/5faac168-7d12-4eed-bd5d-fd1a1706ed78" />

<img width="1379" height="695" alt="Picture2" src="https://github.com/user-attachments/assets/76f5a793-fced-4851-9bac-873d1bebb894" />

Scenario 2. Create a workflow agent in Python
---------------------------------------------

We can create a Python script "web_download_agent.py, to act as an mcp client, to retrieve download history from the query_data_artifacts tool, and then send this to LM Studio/Qwen for analysis. The script creates 5 json files, before submitting the retrieved details to LM Studio (ananyse function). The script saves that output in a markdown file called web_download_report.md

To provide a quicker response from LM Studio, we disable reasoning on the Qwen model, and in the model in LM Studio, in script, "enable_thinking": False". We also set tne max tokens to be returned to 500.
