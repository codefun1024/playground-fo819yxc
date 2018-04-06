# Répéter la vérification

Certains clients de Sécure-IT n'ont pas toute leur tête et oublient fréquemment la combinaison du coffre. Pour les accomoder, le nouveau Coffre-Trop-Fort permet d'essayer des combinaisons tant qu'on n'a pas trouvé la bonne.  Pour répéter une ou plusieurs actions, on utilise ```while``` suivi d'une condition. Tant que cette condition est respectée, les actions qui suivent (décalée vers le droite) sont répétées.

Par exemple, pour répéter une saisie et un affichage tant que l'utilisateur n'aura pas entré «Bonjour», on ferait : 

    message = ""
    while message != "Bonjour":
        print("Non... essayez autre chose")
        message = input("Entrez votre message : ")
		
Remarquez le symbole != qui signifie «différent de». Ainsi, ce qui précède se lit «Tant que le message est différent de "Bonjour", afficher "Non... essayez autre chose" et saisir l'entrée de l'utilisateur.»

@[Répétez la saisie et la vérification de la combinaison tant que l'entrée est différente de la combinaison]({"stubs":["coffre8.py"], "command":"python3 test_coffre8.py"})

Dans cet exemple, l'ordinateur simule les entrées d'un utilisateur. Pour essayer vous-même votre programme avec vos propres entrées, copiez-le dans ce site : [Repl.it/Python3](http://repl.it/languages/python3)
