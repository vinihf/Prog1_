'''

Se uma pessoa corre 10km em 42min e 42s, qual é a média de velocidade em km/hora?

'''

def main():
    distancia_km = 10
    tempo_minutos = 42
    tempo_segundos = 42
    # Converte o tempo total para horas
    tempo_total_horas = (tempo_minutos * 60 + tempo_segundos) / 3600
    # Calcula a velocidade média
    velocidade_media_kmh = distancia_km / tempo_total_horas
    print(f'A velocidade média é de :{velocidade_media_kmh:4.3f} km/h')

if __name__ == '__main__':
    main()