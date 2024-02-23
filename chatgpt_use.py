def chatgpt_connection(prompt):

    import openai

    openai.api_key = "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"

    model_engine = "gpt-3.5-turbo-instruct"  # Updated model engine


    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=800,
        n=1,
        stop=None,
        temperature=0.1
    )

    return completion.choices[0].text




