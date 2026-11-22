---------------------AI integration with local Qwen LLMs and Autopsy 4.23.0----------------

The Autopsy Model Context Protocol (MCP) interface, introduced in Autopsy 4.23.0, provides a read-only interface for querying and summarising open forensic cases using AI clients like Claude Desktop, Claude Code, or local LLM tools such as LM Studio.

To keep AI queries local and private, we will use LM Studio and the Qwen3.5-4b LLM (and Autopsy), in the following example.

https://lmstudio.ai/download/latest/win32/x64
https://lmstudio.ai/models/qwen/qwen3.5-4b

It is necessary to restrict or filter the number of Autopsy Tools that LM Studio sees, when you don't have access to GPU cores. This is done by wrapping a python script, in the mcp json configuration in LM Studio. By restricting LM Studio to the get_server_status and get_data_artifacts, you can comfortably query browser access/downloads. I used an EC2 compute r5.large (16GB).

<img width="523" height="118" alt="Picture1" src="https://github.com/user-attachments/assets/5faac168-7d12-4eed-bd5d-fd1a1706ed78" />

<img width="1379" height="695" alt="Picture2" src="https://github.com/user-attachments/assets/76f5a793-fced-4851-9bac-873d1bebb894" />
