# Vérifier les mauvaises réponses

Pour l'instant, le coffre s'ouvre lorsqu'on donne la bonne combinaison mais il n'affiche aucun message lorsque la combinaison est incorrecte. Pour ajouter un affichage lorsque la condition n'est pas respectée, il suffit d'ajouter ```else:``` sous les lignes ```if``` et ```print``` comme ceci : 

    if condition :
	    print( "Message de réussite" )
	else:
	    print( "Message d'erreur" )

@[Ajoutez un message à afficher lorsque l'utilisateur entre un mot de passe erroné. Le message doit être «Mauvaise combinaison!».]({"stubs":["coffre7.py"], "command":"python3 test_coffre7.py"})

Dans cet exemple, l'ordinateur simule les entrées d'un utilisateur. Pour essayer vous-même votre programme avec vos propres entrées, copiez-le dans ce site : [Repl.it/Python3](http://repl.it/languages/python3)
