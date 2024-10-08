import streamlit as st
import pandas as pd

# Setting up the pages' functions

def menu_principal():
    # Dictionary 

    dicionario = {

    "nome": ['Inteligência Emocional 4.0', 
            'Microsoft Excel - Básico',
            'Iniciação Contábil',
            'Metodologia de escrituração contábil integrada',
            'Plano de contas contábil',
            'Rotinas de auxiliar administrativo',
            'Inteligência Artificial',
            'Python 3 - Mundo 1',
            'Python: noções introdutórias',
            'Certificação Lean Seis Sigma - White Belt',
            'Do R ao H'],
    
    "mes": ['Outubro', 
            'Maio', 
            'Agosto',
            'Agosto',
            'Agosto',
            'Agosto',
            'Junho',
            'Junho',
            'Junho',
            'Maio',
            'Março'],
    
    "instituicao": ['Conquer Business School', 
                    'Fundação Bradesco', 
                    'Cefis',
                    'Cefis',
                    'Cefis',
                    'Cefis',
                    'Conquer Business School',
                    'Curso em Vídeo',
                    'Ada Tech',
                    'FM2S',
                    'Conquer Business School']
    
    }

    df = pd.DataFrame(dicionario)

    # Page's basic configuration 

    st.set_page_config(page_title='Neto Pinheiro', page_icon='neto.png', layout='wide')
    st.logo('resources/neto.png')

    # Links

    ## Button

    st.markdown('# Lourival Teixeira Pinheiro Neto')
    botao = st.link_button('LinkedIn', url='https://www.linkedin.com/in/lourival-pinheiro-7a8744254')

    # Education 

    st.markdown('# Educação')
    st.markdown('---')
    st.markdown('- Administrativo Financeiro - CEBRAC - 2025;')
    st.markdown('- Ciências Contábeis - ANHAGUERA - 2028;')
    st.markdown('- MountainView High School - NEW ZEALAND - 2016.2.')



    # Courses

    st.markdown('# Cursos extracurriculares')
    st.markdown('---')
    st.table(df)

    # Experience 

    st.markdown('# Experiência')
    st.markdown('---')
    texto, imagem = st.columns(2)
    with texto:
        st.write('### TEAM CONTABILIDADE')
        st.caption('Junho de 2024 - O momento')
        st.write('''Com um olhar analítico e proativo, estou construindo uma expertise em Contabilidade e Ciência de Dados. Meu objetivo é identificar oportunidades de melhoria e impulsionar o crescimento financeiro, gerando valor tanto para a minha empresa quanto para nossos clientes.''')
    with imagem:
        st.image('resources/team.jpg')
        
def projetos():

    # Basic configuration 

    st.set_page_config(page_title='Projetos', page_icon='neto.png', layout='wide')

    # Body of the page
    st.markdown('# Projetos')
    st.info('Tenha acesso aos meus projetos em breve.', icon='ℹ')

# Setting up pages

principal = st.Page(menu_principal, title='Neto Pinheiro', default=True)
projeto = st.Page(projetos, title='Informação')

# Navigation Bar

pg = st.navigation(
    {
        "📑 Sobre mim": [principal],
        "📂 Projetos": [projeto]
    }
)

pg.run()