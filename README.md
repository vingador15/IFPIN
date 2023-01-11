# IFPIN
Aplicação web que busca fornecer o mapeamento do IFRJ - Campus Pinheiral, além de informações sobre cada setor, sala, local, turma entre outros<br><br>

<strong>Programas Necessarios</strong> <br><br>
Python(versão mais recente e estável possível) <br>
Postgresql + extensão Postgis <br>
Biblioteca GDAL + python-gdal <br>
VSCode ou PyCharm(Não testei em outros programas, porém não é uma regra :D) <br>
PGAdmin4(Opcional caso não queira trabalhar com o terminal)

<strong>Configuração do Banco de dados</strong><br><br>

[Após ter criado um novo usuário postgres e inserido uma senha a ele]<br>


<strong>1º Caso - Usando o Terminal</strong><br>

[Dica: crie um usuário com o mesmo nome do usuário do computador assim não precisará fazer login]

<code>
  $ psql [Seu Banco de Dados]<br>
  $ create extension postgis;
</code><br>

<strong>2º Caso - Usando o PGAdmin4</strong><br><br>

Abra o programa<br>
Faça login com o usuário postgres que você criou<br>
Crie um novo banco de dados<br>
Habilite a extensão postgis<br><br>

<strong>Passos para rodar a aplicação</strong><br><br>

1 - Crie um ambiente virtual(venv) na raiz do projeto e ative-a<br>
2 - Instale as dependencias com o comando <code>(venv)$ pip install -r requirements.txt</code><br>
3 - Configure o arquivo env-não-finalizado:
<ul>
      <li> SECRET_KEY --> insira uma chave de segurança forte ou crie um outro projeto django e copie a chave desse outro projeto <li>
      <li> DEBUG --> enquanto estiver desenvolvendo deixe em True caso contrario ponha False </li>
      <li> ALLOWED_HOSTS --> insira apenas <code>127.0.0.1, .localhost, [SeuIp, caso queira abrir no celular]</code> </li>
      <li> DATABASE_URL --> insira <code>postgres://[Seu Usuário]:[Senha]@localhost/[Nome do BD]</code></li>
      <li> Após configurar renomeie o arquivo para .env </li>
</ul><br>
4 - No terminal digite<br>
<code>
  $ python manage.py shell<br>
  >>>from Mapa.load import run_locais<br>
  >>>run_locais()
</code><br>
Caso apareça uma lista escrito <code>Saved: [nome de um local]</code> significa que deu certo<br>
5 - Delete os campos Lugar e Salas de login.forms<br>
6 - No terminal digite <code>$ python manage.py makemigrations</code> e <code>python manage.py migrate</code><br>
7 - Reinsira os campos Lugar e Salas de login.forms<br>
8 - Crie um superusuario com o comando <code>$ python manage.py createsuperuser</code><br>
9 - Por fim inicie o servidor com <code>$ python manage.py runserver</code> e em seu navegador acesse localhost:8000<br>
