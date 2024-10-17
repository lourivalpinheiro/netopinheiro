import streamlit as st
import pandas as pd
import plotly.express as plt

# Setting up the pages' functions

def curriculo():
   

    df = pd.read_excel('files\data.xlsx')

    # Page's basic configuration 

    st.set_page_config(page_title='Neto Pinheiro', page_icon='neto.png', layout='wide')


    # Button

    st.markdown('# Lourival Teixeira Pinheiro Neto')
    botao = st.link_button('LinkedIn', url='https://www.linkedin.com/in/lourival-pinheiro-7a8744254')

    # Em destaque
    
    st.markdown('### Em destaque')
    st.page_link('https://ltpneto.streamlit.app/lifelong_learning', label='Lifelong Learning', icon='🧠')

    # Education 

    st.markdown('# Educação')
    st.markdown('---')
    st.markdown('- Administrativo Financeiro - CEBRAC - 2025;')
    st.markdown('- Ciências Contábeis - ANHAGUERA - 2028;')
    st.markdown('- MountainView High School - NEW ZEALAND - 2016.2.')



    # Courses

    st.markdown('# Cursos extracurriculares')
    st.markdown('---')
    st.dataframe(df)

    # Experience 

    st.markdown('# Experiência')
    st.markdown('---')
    texto, imagem = st.columns(2)
    with texto:
        st.write('### TEAM CONTABILIDADE')
        st.caption('Junho de 2024 - O momento')
        st.write('''Com um olhar analítico e proativo, estou construindo uma expertise em Contabilidade e Ciência de Dados. Meu objetivo é identificar oportunidades de melhoria e impulsionar o crescimento financeiro, gerando valor tanto para a minha empresa quanto para nossos clientes.''')
    with imagem:
        st.image(r'files\images\team.jpg')

def cursos():
    
    # Data

    df = pd.read_excel('files\data.xlsx')
    df2 = df[['mes', 'carga_horaria']]
    df3 = pd.read_excel('files\data.xlsx', sheet_name= 'curso_mes')
    df4 = pd.read_excel('files\data.xlsx', sheet_name='orcado')
    

    # Body of the page

    ## Basic configuration

    st.set_page_config(page_title='Projetos', page_icon='neto.png', layout='wide')

    # Body of the page

    st.markdown('# Conhecimento')   
    st.caption('Fique por dentro de tudo que concerne meus estudos.')
    
    st.markdown("## Cursos extra-curriculares")
    st.table(df)

    # Analises

    analise_horas, qtd_curso = st.columns(2)
    with analise_horas:
        st.markdown('## Quantidade de horas de estudo:')
        fig1 = plt.bar(df2, x='mes', y='carga_horaria')
        st.plotly_chart(fig1)
    
    with qtd_curso:
        st.markdown('## Quantidade de cursos por mês:')
        fig2 = plt.bar(df3, x='mes', y='quantidade')
        st.plotly_chart(fig2)

    st.markdown('## Dados sobre orçamento planejado para educação em 2024:')
    st.markdown('---')
    fig3 = plt.box(df4, y='valor')
    st.plotly_chart(fig3)

    
def projetos():

    # Basic configuration 

    st.set_page_config(page_title='Projetos', page_icon='neto.png', layout='wide')

    # Body of the page
    st.markdown('# Projetos')
    st.info('Tenha acesso aos meus projetos em breve.', icon='ℹ')

def lifelong_learning():
    st.set_page_config(page_title='Neto Pinheiro', page_icon='neto.png', layout='centered')
    
    st.markdown('# Aprendizado Contínuo: a chave para o sucesso profissional no século XXI')
    st.feedback("thumbs")
    st.markdown('## Introdução')
    st.markdown('''
                ---
                Em um mundo em constante transformação, a educação tradicional muitas vezes se mostra insuficiente. 
                No Brasil, [dados recentes](https://www.britannica.com/place/Brazil/Primary-and-secondary-school) revelam um número alarmante de jovens  não conclui a educação básica, 
                comprometendo seu futuro profissional.
                ''')
    st.markdown('''
                ## Lifelong Learning
                ---
                Aprendizado contínuo é a prática ou filosofia que visa adquirir novos conhecimentos e habilidades ao longo de toda a vida,
                seja através de cursos, leituras, experiências práticas ou interações com outras pessoas. Em uma perspectiva focada no trabalho,
                o que faz dessa filosofia uma ferramenta tão poderosa para aqueles que usufruem dela é o irrefutável fato de que profissionais 
                que não se atualizam tendem a ficar obsoletos frente aos concorrentes no mercado de trabalho.
                ''')
    st.markdown('''
                ## A importância e benefícios do Aprendizado Contínuo
                ---
                Você já se perguntou por que algumas pessoas se destacam em suas carreiras, enquanto outras parecem estagnar?
                A resposta pode pode estar na busca constante por conhecimento. Uma das habilidades mais valorizadas pelo mercadod de trabalho
                é a resolução de problemas. Por buscarem conhecimento de diferentes áreas, pessoas que colocam em prática essa ideia 
                tendem a ter um arsenal mais preparado para lidar com desafios, quando eles aparecem. Com o tempo, como qualquer ativo, esses conhecimentos
                são aprofundados e criam conexões por pontos comuns entre si, tornando o aprendiz cada vez mais capaz de unir conceitos e utilizá-los no dia a dia,
                além de perceber os seguintes benefícios: \n

                1. Adaptabilidade: Os aprendizes contínuos são mais adaptáveis às mudanças do mercado de trabalho, pois estão sempre atualizados sobre 
                as últimas tendências e tecnologias; \n
                2. Inovação: A busca por novos conhecimentos estimula a criatividade e a capacidade de "pensar fora da caixa", gerando novas ideias e soluções; \n
                3. Satisfação pessoal: Além dos benefícios profissionais, o aprendizado contínuo contribui para o desenvolvimento pessoal, aumentando a autoestima e o bem-estar.
                ''')
    st.markdown('''
                ## Aprendizado Contínuo não é "generalismo"
                ---
                Lifelong learners não são generalistas. Embora o aprendizado contínuo abranja diversas áreas, é fundamental ter uma eespecialização em um 
                determinado campo. A combinação de conhecimento profundo, amplitude e humildade para saber que é necessário obter conhecimento de diferentes áreas
                para resolver questões é o que diferencia um profissional de sucesso.
                ''')
    st.markdown('''
                ## Conclusão
                ---
                Pense em um médico que busca se atualizar sobre as últimas pesquisas em sua área, ou um progamador que aprende uma nova linguagem de programação.
                Esses são exemplos de profissionais que investem em seu desenvolvimento contínuo. Quanto mais avançamos, mais vai ficando clara a percepção
                de que precisamos de pessoas dispostas a ir além de seus conhecimentos atuais para resolverem problemas que nos impactam como sociedade. 
                O futuro pertence aos eternos aprendizes. Mudamos o mundo ao transformar as nossas mentes.
                ''')


# Setting up pages

principal = st.Page(curriculo, title='Currículo', default=True)
knowledge = st.Page(cursos, title='Cursos')
projeto = st.Page(projetos, title='Informação')
lifelong = st.Page(lifelong_learning, title='Lifelong Learning')

# Navigation Bar

pg = st.navigation(
    {
        "📑 Sobre mim": [principal],
        "📰 Artigos": [lifelong],
        "📚 Conhecimento": [knowledge],
        "📂 Projetos": [projeto]
    }
)

pg.run()
