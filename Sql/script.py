import _mysql

cnx = _mysql.connect(
    user='root',
    host='127.0.0.1',
    db='chevre'
)

result = cnx.query('INSERT INTO `utilisateur`(`id`, `nom`, `prenom`, `email`, `date_naissance`, `pays`, `ville`, `code_postal`) VALUES (1, "Queen", "Oliver", "arrow@teamarrow.com", "1980/05/28", "Na ilha", "This City", "12345")')

