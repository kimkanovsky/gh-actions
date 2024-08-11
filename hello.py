'''Module performs simple division and merges two dictionaries.'''

import logging

# Настройка базового конфигурации логирования
logging.basicConfig(level=logging.INFO)

asd = 1
bsd = 2
csd = asd / bsd
dsd = {'hello': 'world'} | {'foo': 'bar'}

def main() -> None:
    """Run the main logic of the module."""
    
    # Используем логирование вместо print
    logging.info('Result of division: %s', csd)

if __name__ == '__main__':
    main()
