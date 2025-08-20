from flask import render_template, request, redirect, url_for
from app import app
from app.models.produtos_loja import produtos_loja, carrinho, adicionar_produto


@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    if request.method == "POST":
        produto = request.form.get("produto")

        if produto:  # garante que não é None
            produto = produto.lower().strip()

            if produto == "sair":
                return redirect(url_for("resumo"))

            sucesso, valor = adicionar_produto(produto)
            if sucesso:
                mensagem = f"Você escolheu {produto}: {valor} R$"
            else:
                mensagem = "Produto inválido"

    return render_template(
        "index.html", produtos=produtos_loja, mensagem=mensagem, carrinho=carrinho
    )


@app.route("/resumo")
def resumo():
    if not carrinho:
        return render_template("resumo.html", mensagem="Carrinho vazio!")

    precos = [preco for _, preco in carrinho]
    total = sum(precos)
    media = total / len(precos)
    mais_caro = max(carrinho, key=lambda x: x[1])
    mais_barato = min(carrinho, key=lambda x: x[1])

    return render_template(
        "resumo.html",
        carrinho=carrinho,
        total=total,
        media=media,
        mais_caro=mais_caro,
        mais_barato=mais_barato
    )
