# DataedoChat 💬❄️

Interact with your Snowflake database using natural language queries

User-friendly application that enables users to interact with their Snowflake DataBase using natural language queries.

![image](https://github.com/maciejbrasewicz/edo-chat/assets/49028274/581b9fdc-a94c-4ec8-a019-d7313b60158a)


## Here is the link to the [EdoChat](https://edo-chatgit-lqmmwz4upu.streamlit.app/)


EdoChat leverages OpenAI's GPT model to convert natural language into SQL queries, making it ideal for users who may not have a firm grasp of SQL syntax. And it has a  transformative impact on data interaction by expediting and streamlining data-driven decision-making.

Let's take a look at the tech stack on which the chat is built:

- `Streamlit`: The UI magic
- `Snowflake`: The database powerhouse
- `GPT-3.5 and LangChain`: The language model maestros
- `Supabase`: The vector database virtuoso

Here's a glance at snowChat's architecture:

![image](https://github.com/maciejbrasewicz/edo-chat/assets/49028274/b2b41e69-2d47-4e20-9ba4-f4a373f6a9e6)


## 🌟 Features

- **Conversational AI**: Harnesses ChatGPT to translate natural language into precise SQL queries.
- **Conversational Memory**: Retains context for interactive, dynamic responses.
- **Snowflake Integration**: Offers seamless, real-time data insights straight from your Snowflake database.
- **Self-healing SQL**: Proactively suggests solutions for SQL errors, streamlining data access.
- **Interactive User Interface**: Transforms data querying into an engaging conversation, complete with a chat reset option.

## 🛠️ Installation

To start, follow these steps:

1. Clone this repository:
   git clone `https://github.com/maciejbrasewicz/edo-chat`

2. Install the required packages:
```
   cd edo-chat
   pip install -r requirements.txt
```
3. Get the Data Definition Language (DDL) for all tables from `snowflake.account_usage.tables`.

4. Use ChatGPT to convert the DDL to markdown format.

5. Store the schema files for each table in the docs/ folder.

6. Create an account with [Supabase](https://supabase.com/?ref=blog.streamlit.io), set up a free database, and configure environment variables for the .streamlit folder in secrets.toml (remember to include your Snowflake credentials).

Your final secrets.toml should look like this:
```
OPENAI_API_KEY= "your openAI API key"
[streamlit]
SUPABASE_URL = "<https://yourapp.supabase.co>"
SUPABASE_SERVICE_KEY = "your Supabase key"

[snowflake]
ACCOUNT = "youraccount"
USER_name = "youruser"
PASSWORD = "yourpassword"
DATABASE = "yourdatabase"
SCHEMA = "yourschema"
WAREHOUSE = "yourwarehouse"
ROLE = "your snowflake role"
```

7. Run the Supabase scripts found under supabase/scripts.sql in the Supabase SQL editor to activate the pgvector extension, create tables and set up a function.

8. Run python ingest.py to convert your documents into vectors and store them in the Supabase table named 'documents.'

The 'documents' table in Supabase should look like this:

![image](https://github.com/maciejbrasewicz/edo-chat/assets/49028274/4cddc601-55f2-4c6b-b755-ce1138921b6b)


9. Run the Streamlit app to start chatting:
   `streamlit run main.py`


## 🚀 Additional Enhancements

1. **Platform Integration**: Connect chat with popular communication platforms like Slack or Discord for seamless interaction.
2. **Voice Integration**: Implement voice recognition and text-to-speech functionality to make the chatbot more interactive and user-friendly.
3. **Advanced Analytics**: Integrate with popular data visualization libraries like Plotly or Matplotlib to generate interactive visualizations based on the user's queries (AutoGPT).


## License

This project uses the following license: [MIT License](https://opensource.org/licenses/MIT).

## Contact

You can reach me at `maciej.brasewicz@gmail.com`.
