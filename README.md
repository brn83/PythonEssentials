# PythonEssentials

*** Treinamento da Linuxtips.io ***


PLR - Python Language Reference
    (documento de referência)

Implementação -  Implentações para rodar a liguagem
    CPython (oficial); 
    IronPython(.Net); 
    Jython(JVM);
    PyPy(JIT compiler); 
    Stackeless Python (CPython supporting microthreads);
    MicroPython (running on micro controllers);

Ecossistema - ..., Comunidades (PSF), Pacotes e Ferramentas (pypi.org)

Onlines IDEs

* replit.com
* gitpod.io

## Aula 2
 
 Comandos para usar o python direto no terminal
 Exemplo 1:
```
> python3 -c "print('bruno'.upper())"

```
Exemplo 2:
```
> python3 -c "print(45-36)"
```

Comando que retorna as informações de instalação do pyhton no ambiente:
```
> python3 -m site
```

Ambiente de apredizagem do Python com exemplos de código:
```
> python3 -m turtledemo
```

Entrar no terminal interativo do Python (REPL - Read-Eval-Print-Loop):
```
> python
```

Para entrar na ajudar interativa use help:

```
> help ()
```

No Promt do help é possivel consultar os módulos instalados:

```
help> modules
```

Tópicos de ajuda no prompt do help:
```
help> topics
```

Para sair use a letra 'q':
```
help> q
```

### IDEs

*  [Micro](https://micro-editor.github.io)
* [VS Code](https://code.visualstudio.com)

## Aula 3

### GIT

Siga os passos abaixo para gerar um nova chave SSH:
```
ssh-keygen -t ed25519 -C "seu_email@gmail.com"
```

Então, inicie o ssh-agent em segunto plano:
```
eval "$(ssh-agent -s)"
```

Adicionar a chave SSH privada ao agente ssh:
```
cd 
```
 ou (em versões antigas do OS):
```
ssh-add -A .ssh/id_ed25519
```
Criar o arquivo config:
```
touch .ssh/config
```
Listar as váriaveis de ambeinte:
```
env
```
Executando o arquivo direto:

1. especificar no Shebang as informações de ambiente:
```
#!/usr/bin/env python3
```
2. Rodar o arquivo diretamento no terminal:
```
./hello.py
```
Adicionar permissão para rodar o arquivo direto do terminal:
```
chmod +x hello.py
```
