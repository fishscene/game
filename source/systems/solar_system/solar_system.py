import controller, model, view

class SolarSystem(controller.Controller, model.Model, view.View):
    def __init__(self, parent=None):
        controller.Controller.__init__(self)
        model.Model.__init__(self, parent)
        view.View.__init__(self)
