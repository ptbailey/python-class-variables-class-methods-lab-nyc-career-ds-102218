
class Driver:
    _all = []
    _count = 0

    def __init__(self,_name, _car_make, _car_model):
        self._name = _name
        self._car_make = _car_make
        self._car_model = _car_model
        Driver._all.append(self)
        Driver._count += 1

    @classmethod
    def fleet_size(cls):
        return cls._count

    @classmethod
    def driver_names(cls):
        names = []
        for driver in cls._all:
            names.append((vars(driver))['_name'])
        return names

    @classmethod
    def fleet_makes(cls):
        names = []
        for make in cls._all:
            names.append((vars(make))['_car_make'])
        return names

    @classmethod
    def fleet_models(cls):
        names = []
        for model in cls._all:
            names.append((vars(model))['_car_model'])
        return names

    @classmethod
    def fleet_makes_count(cls):
        list_of_makes = cls.fleet_makes()
        unique_list = set(list_of_makes)
        dict_unique_list = dict.fromkeys(unique_list,0)
        for make in list_of_makes:
            dict_unique_list[make] += 1
        return dict_unique_list

    @classmethod
    def fleet_models_count(cls):
        list_of_models = cls.fleet_models()
        unique_list = set(list_of_models)
        dict_unique_list = dict.fromkeys(unique_list,0)
        for model in list_of_models:
            dict_unique_list[model] += 1
        return dict_unique_list

    @classmethod
    def percent_of_fleet(cls,name):
        car_count = (cls.fleet_makes_count())[name]
        # total_count = sum(list((cls.fleet_makes_count).values()))
        percent = round((car_count/cls._count)*100,3)
        return f'{percent}%'
