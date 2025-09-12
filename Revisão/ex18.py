import requests


def buscar_endereco(cep):
    cep_formatado = str(cep).strip().replace("-", "").replace(".", "")

    if not cep_formatado.isdigit() or len(cep_formatado) != 8:
        print(f"erro: o cep {cep} é inválido")
        return

    url = f"https://viacep.com.br/ws/{cep_formatado}/json/"

    try:
        print(f"buscando informação para o cep {cep_formatado}")
        reposta = requests.get(url, timeout=5)

        if reposta.status_code == 200:
            dados = reposta.json()

            if dados.get("erro"):
                print("cep não encontrado")
                return

            print("\n--- Endereço Encontrado ---")
            print(f"Logradouro: {dados.get('logradouro')}")
            print(f"Bairro: {dados.get('bairro')}")
            print(f"Cidade: {dados.get('localidade')}")
            print(f"Estado: {dados.get('uf')}")
            print(f"Região: {dados.get('regiao')}")
            print(f"DDD: {dados.get('ddd')}")
            print("---------------------------\n")
        elif reposta.status_code == 400:
            print("erro: 400. requisição mal formatada")
        else:
            print(f"erro na requisição. código de status {reposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"ocorreu um erro na conexão {e}")


if __name__ == "__main__":
    cep_digitado = input("digite um cep: ")
    buscar_endereco(cep_digitado)
