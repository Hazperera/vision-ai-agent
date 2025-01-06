from vision_agent.agent import VisionAgent
import os

api_key = os.getenv("OPENAI_API_KEY")

agent = VisionAgent(verbosity=2)
resp = agent("Hello")
print(resp)

# Initialize resp as a list of dictionaries
resp_list = [
    {
        "role": "user",
        "content": resp
    }
]

resp_list.append(
    {
        "role": "user", 
        "content": "Can you count the number of fingers in this image?", 
        "media": [
            "vision-ai-agent/data/sample_hand_images/Hand1.png",
            "vision-ai-agent//data/sample_hand_images/Hand2.png",
            "vision-ai-agent//data/sample_hand_images/Hand3.png",
            "vision-ai-agent//data/sample_hand_images/Hand4.png",
            "vision-ai-agent//data/sample_hand_images/Hand5.png",
            "vision-ai-agent//data/sample_hand_images/Hand6.png"
        ],
    }
)

resp = agent(resp_list)
print(resp)











# from vision_agent.agent.vision_agent_coder_v2 import VisionAgentCoderV2
# from vision_agent.tools import load_image
# import PIL.Image


# agent = VisionAgentCoderV2(verbosity=2)
# code = agent("Count the number of fingers in this image", media=image_path)

# image_path = "data/sample_hand_images/Hand1.png"
# user_prompt = """
# Write a program that segment palm and fingers in an image. 
# The program should draw bounding boxes around each detected fingers and 
# the palm and display the confidence score for each prediction. 
# """

# messages = [
#     {
#         "role": "user",
#         "content": user_prompt,
#         "media": [image_path],
#     }
# ]
# response = agent.generate_code(messages)
