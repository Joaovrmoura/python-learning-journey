# Funções decoradoras e decoradores
# decorar = adicionar / remover / Restringir / alterar
# decoradores são usados para fazer o python
# usar as funções decoradoras em outras funções
# Decoradores são "Syntax Sugar" (açucar da sintático)

#Função decoradora
def create_function(func):
    def inside(*args, **kwargs):
        print('Decorando a Função')
        for arg in args:
            is_string(arg)
            print('decorando...')
        result = func(*args, **kwargs)
        result += ' LOL'
        print('Função decorada seu valor é', result)
        return result
    return inside
# Função decoradora

# decorador passa essa função para a função decoradora
@create_function
def reverse_string(string):
    print(reverse_string.__name__)
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param should be a string')
    
    
# check_string_parameter = create_function(reverse_string)
reversed = reverse_string('123')
print(reversed)
