import openai

print("Welcome! This is a software that generates image according to your description")
openai.api_key = input("Please input your openai api key:")

while True:
    proceed = input("Do you want to generate an image? (Y/N):")
    if proceed == "Y":
        prompt = input("Please enter your prompt:")
        response = openai.Image.create(
            prompt=prompt, n=1, size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print("Here is the url of the image:", image_url)
    elif proceed == "N":
        break
    else:
        print("Please enter Y or N.")



