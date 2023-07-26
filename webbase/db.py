class DBBudgetRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = (
        # "aaa",
        # "formula_aaa",
        # "bvs",
        # "formula_bvs",
        # "vcs",
        # "formula_vcs",
        # "budgetapp",
        # "budget_vcst",
        "budgetapp"
    )

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """

        if model._meta.app_label == "inventoryapp":
            return "budget_vcst"
        
        if model._meta.app_label == "budgetapp":
            return "budget_vcs"
        
        if model._meta.app_label == "budgetaaa":
            return "budget_aaa"
        
        if model._meta.app_label == "budgetbvs":
            return "budget_bvs"

        if model._meta.app_label == "formulavcst":
            return "formula_vcst"
        
        if model._meta.app_label == "formulavcs":
            return "formula_vcs"

        return "default"

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label == "inventoryapp":
            return "budget_vcst"
        
        if model._meta.app_label == "budgetapp":
            return "budget_vcs"
        
        if model._meta.app_label == "budgetaaa":
            return "budget_aaa"
        
        if model._meta.app_label == "budgetbvs":
            return "budget_bvs"

        if model._meta.app_label == "formulavcst":
            return "formula_vcst"
        
        if model._meta.app_label == "formulavcs":
            return "formula_vcs"

        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        print("Allow relations if a model in the auth or contenttypes apps")
        # if (
        #     obj1._meta.app_label in self.route_app_labels
        #     or obj2._meta.app_label in self.route_app_labels
        # ):
        #     return True

        # if (
        #     obj1._meta.app_label == "budgetapp"
        #     or obj2._meta.app_label == "budgetapp"
        # ):
        #     return True

        # return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """

        if app_label == "budgetapp":
            return None
        
        if app_label == "budgetaaa":
            return None
        
        if app_label == "budgetbvs":
            return None

        if app_label == "formulavcs":
            return None
        
        if app_label == "formulavcst":
            return None
        
        if app_label == "inventoryapp":
            return None

        return True
