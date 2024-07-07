mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"jcnw@pop06.odn.ne.jp\"\n\
" > ~/.streamlit/credential.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
