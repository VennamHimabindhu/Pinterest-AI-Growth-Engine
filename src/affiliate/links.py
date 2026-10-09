from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from src.affiliate.models import Product


def validate_product(product: Product):
    if not product.product_id:
        return False, "Product ID is missing."

    if not product.name:
        return False, "Product name is missing."

    if not product.category:
        return False, "Product category is missing."

    parsed_url = urlparse(product.product_url)

    if parsed_url.scheme not in {"http", "https"}:
        return False, "Product URL must use HTTP or HTTPS."

    if not parsed_url.netloc:
        return False, "Product URL is invalid."

    return True, "Product is valid."


def build_affiliate_link(product: Product, affiliate_tag: str):
    is_valid, message = validate_product(product)

    if not is_valid:
        raise ValueError(message)

    if not affiliate_tag:
        raise ValueError("Affiliate tag is missing.")

    parsed_url = urlparse(product.product_url)

    query_params = parse_qs(parsed_url.query)
    query_params["tag"] = [affiliate_tag]

    new_query = urlencode(query_params, doseq=True)

    affiliate_url = urlunparse(
        (
            parsed_url.scheme,
            parsed_url.netloc,
            parsed_url.path,
            parsed_url.params,
            new_query,
            parsed_url.fragment,
        )
    )

    return affiliate_url


if __name__ == "__main__":

    product = Product(
        product_id="demo-001",
        name="Minimalist Skincare Set",
        category="Skincare",
        product_url="https://example.com/product/demo-001",
    )

    is_valid, message = validate_product(product)

    print("VALIDATION:")
    print(is_valid, "-", message)

    affiliate_link = build_affiliate_link(
        product,
        "demo-affiliate-tag",
    )

    print("\nAFFILIATE LINK:")
    print(affiliate_link)