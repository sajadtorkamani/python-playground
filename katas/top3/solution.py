# So cryptic... me no like
def top3(products, amounts, prices):
    totals = {}

    for index, product in enumerate(products):
        totals[product] = amounts[index] * prices[index]

    return [pair[0] for pair in sorted(totals.items(), key=lambda x: x[1], reverse=True)[:3]]


"""
JavaScript equivalent is so much more readable
const top3 = (products, amounts, prices) = > {
    return products
      .map((product, index)=> ({
          name: product,
          sale: amounts[index] * prices[index]
      }))
      .sort((a, b)=> b.sale - a.sale)
      .slice(0, 3)
      .map(product= > product.name)
}
"""
