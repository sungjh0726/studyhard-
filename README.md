# Title 1 : Install Oracale-XE

  Docker Terminal을 실행시킵니다.
  
 $> docker search oracle
 
   -> Docker에서 oracle이라는 프로그램을 먼저 검색합니다. 검색한 oracle 목록에서 star수가 많은것중에 oracle 무료 버젼인 sath89/oracle-xe-11g를 확인합니다.
   
 $> docer pull sath89/oracle-xe-11g
 
   -> 검색 확인 했었던 sath89/oracle-xe-11g 파일을 다운로드합니다.
   
 $> docker run -d --name ora1 -p 8080:8080 sath89/oracle-xe-11g
 
   -> docker에서 실행시키는데 -d하고 이름은 ora1로 지은 oracle파일을 외부의 8080와 pull 받은 docker container의 8080 포트와 연결시킵니다.
   
 $> docker ps
 
   -> docker가 잘 띄워졌는지 확인합니다.
   
 $> docer exec -it ora1 bash
 
   -> ora1이라는 컨테이너를 화면에(input status) 실행(exec) 시킵니다(bash; 명령)

# Tiltle 2 : Install MySQL 5.7 by Docker

 Docker Terminal을 실행시킵니다.
 
 $> docker search mysql
 
    -> docker에서 mysql를 찾아봅니다.
    
 $> docker pull mysql : 5.7
 
    -> docker search를 통해 찾은 mysql 버젼을 확인하고 해당버젼을 다운로드합니다.
    
 $> docker images
 
    -> 다운받은 mysql를 image로 떠놓습니다.
    
 $> docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=V! --name mysql57 mysql:5.7
 
      -> dockerdp mysql57이라는 컨테이너를 3306포트를 통해(-p 3306:3306) 연결해서 실행(run)할건데 실행할때 패스워드는 v!(MYSQL_ROOT_PASSWORD=V!)         로 할겁니다.
      
 $> docker ps
 
    -> dockr가 잘 띄워졌는지 확인합니다.
    
 $> docker exec -it mysql57 bash
 
    -> mysql57이라는 컨테이너를 실행시킵니다.
    
 # Title 3 : Write a separate process for creating databases and users on Oracle.
 
 $> docker start mysql 57
 
    -> mysql57를 구동시킵니다.
    
 $> docker exec -it mysql 57 bash
 
    -> mysql57를 실행(exec)시킵니다.
    
 #> mysql -u root -p
 
    -> mysql를 root 계정과 연결합니다.
    
 mysql> create database hardsql
 
    -> hardsql이라는 데이터베이스(이하 DB)를 만듭니다.
    
 mysql> show databases;
 
    -> DB가 만들어졌는지 확인합니다.
    
 mysql> use hardsql
 
    -> hardsql를 사용합니다.
    
 mysql> create user goodsql@'%'identified by 'good';
 
    -> user 이름은 모든것을 기반(%)한 goodsql로 하고 그 user의 pw는 good으로 한다.
    
 mysql> grant all privilages on *.* to 'goodsql'@'%';
 
    -> 모든 것을 기반한 goodsql user에게 모든권한(*.*)을 부여한다.
    
* mysql> grant all privilage on gooddb.* to 'goodsql'@'%';

     -> goodsql 유저에게 모든 DB중 gooddb에 관한 DB의 권한만 부여한다.
     
 mysql> flush privilages;
 
    -> 지금까지 설정한 user내용과 DB권한 부여한것을 저장한다.
    
    
    
 

 # Title 4 . Docker의 개념과 구성요소 (Image, Container, Docker-machine 등)에 대해 본인이 이해한 바를 자유롭게 서술하고, Docker의 설치과정과              정상 설치를 확인하는 과정을 기술하시오
  
   * 예전에는 HOST OS(window,Mac) 위에 서버를 각각 구현하였다면 지금은 docker를 이용해서 서버를 용이하게 구현할 수 있게 됐다.
   
  예를 들어 한 서버에 WAHS,DB,GIT 등 여러가지 설치파일을 놓았을때 이 서버에서 설치된 것들을 다른 서버에도 옮기려면 예전에는 일일히 다 설치해야 됐다. 하지만 지금은 이렇게 만들어진 서버(container)를 간편한 image로 떠서 갖고 다른 서버에 image를 붙이기만 하면 처음 A서버에 설치햇던 파일들을 편리하게 설치할수 있게 된것이다.
  
   여기에서 Docker 보다 밖에 있는 것을 Docker client라고 한다.
   
   그리고 이 Docker image는 자유롭게 만들 수 있고(Build) 밖의 디렉토리와 파일을 공유(ship) 할 수도 있다.
   
  * Docker 설치과정
  
    docker docs의 window용 docker에 들어가서 docker toolbox를 다운받는다.
    
  
  * Docker 정상설치 
  
    docker 터미널을 실행시킨다.
    
 $> docker -version
 
    -> docker의 버젼을 확인한다.
    
 $> docker run hello - world
 
    -> Docker Hub에 있는 hello-world image를 실행시킨다.
    
 $> docker image ls
 
    -> image list에 hello-world가 정상 다운되었는지 확인한다.
    
 $> docker ps
 
    -> 띄워져있는 docker image를 확인한다.
    
    
    
 # Title 5 . Linux(Ubuntu) Docker Container를 구동하기 위한 절차를 쓰고, 설치된 Ubuntu Container에 Telnet daemon 구동하기, 한글 사용 설정하            기, Git 사용 설정하기 등의 작업절차를 기술하시오
 
 1)  Linux(Ubuntu) Docker Container를 구동하기 위한 절차
 
 
 $> sudo qpt-get install openjdk-8-jdk-y
 
    -> ubuntu를 apt-get에서 설치한다.
    
 $> docker container run ubuntu :latest
 
    -> 설치된 ubuntu를 구동시킨다.
    
 $> docker run -itd --name ub ubuntu bash
 
    ->ub라는 Ubuntu를 docker에서 실행시킨다.
    
    
 2) Telnet daemon 구동하기
 
 $> sudo apt-get install xinetd telnetd
 
    -> apt-get에서 telnet을 설치한다.
    
 $> vi /etc/xinetd.d/telnet
 
    -> telnet daemon을 구동하기 위해 telnet 설정창을 vi를 실행시켜 설정한다.
    
 
 
 ---vi 화면---
 
 service telnet
 
 {
 
    disable = no
    
    flages = REUSE
    
    socket-type = stream
    
    wait = no
    
    user = roof
    
    sever = /usr/sbin/intelnetd
    
    log_on.failure +=USCRID
    
 }
 
       -> vi에 위와같이 적고 :wq를 입력하고 나온다.
       
 
 
 $> /etc/init.d/xinetd restart
 
    ->telnet Daemon이 잘 구동되는지 재시작해본다.
    
 $> docker commit ub ub_telnet
 
    -> 잘 구동되는 ub_telnet을 저장한다.
    
 $> docker run -itd -p 23:23 --name ubt ub_telnet bash
 
    -> ubt라고 이름지어진(--name ubt) ub_telnet을 23port(-p 23:23)에 연결하여 실행(run) 시킨다(bash)
    
 
 
 3) 한글 사용 설정하기
 
 $> apt-get install locales
 
    -> 언어설정할 locales를 설치한다.
    
 $> locale -a
 
    -> locale에서 적용가능한 언어를 찾는다.
    
  #LC_ALL = ko_KR.utf-8 bash
  
    ->locale을 치면 LC_ALL이 비어져있을 것이다. 이 비어져있는 곳에 ko.KR.utf-8(한국어)를 넣어준다.
    
    
    
 4) git 사용 설정하기
 
 #> apt-get install git
 
    -> apt-get 에서 git을 설치한다.
    
 #> git config--global user.name sungjh0726
 
    ->sungjh0726이라는 git user name을 기록(설정)한다.
    
 #> git config --global user.email sungjh0726@naver.com
 
    ->sungjh0726@naver.com이라는 email를 기록한다.
    
 #> git clone https://github.com/sungjh0726/studyhard
 
    ->studyhard라는 repository url를 연결시켜준다
    
 #> git config credetial.helper store.
 
    ->git을 실행할때 마다 나오는 로그인정보를 저장하여 다음에 push할때 자동로그인을 할 수 있게 해준다.
    
