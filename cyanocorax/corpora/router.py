# IDefinición de un router de base de datos para mongodb


class CorporaRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'corpora':
            return 'cyanocorax'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'corpora':
            return 'cyanocorax'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if (obj1._meta.app_label == 'corpora' and
                obj2._meta.app_label == 'corpora'):
            return True
        elif ('corpora' not in
                [obj1._meta.app_label, obj2._meta.app_label]):
            return True
        return False

    def allow_syncdb(self, db, model):
        if (db == 'cyanocorax' or
                model._meta.app_label == "corpora"):
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True
