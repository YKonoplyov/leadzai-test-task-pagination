def test_parametrizer(params_names_str: str, params_values: list[list]) -> callable:
    params_names_list = params_names_str.split(',')
    def decorator(test_case: callable) -> callable:
        def parameterizer(self, *args, **kwargs) -> None:
            for params in params_values:
                params_dict = dict(zip(params_names_list, params))
                
                test_case(self, **params_dict)
        return parameterizer
    return decorator
