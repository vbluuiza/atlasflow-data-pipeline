from extract.extract_data import connect_mongo, create_connect_db, create_connect_collection
from transform.transform_data import visualize_collection, rename_columns, select_category, make_regex, create_dataframe, rename_df_columns, format_date
from load.load_data import insert_data, save_csv

if __name__ == '__main__':
    
    # 1. Connect to MongoDB
    client = connect_mongo()
    db = create_connect_db(client, "test_database")
    collection = create_connect_collection(db, "collection_products")
    
    #2. Insert test data
    data = [
        {
            "Produto": "Livro Python Fluente",
            "Categoria do Produto": "Livros",
            "Preço": 89.90,
            "Frete": 5.90,
            "Data da Compra": "15/04/2023",
            "Vendedor": "Amazon",
            "Local da compra": "Online",
            "Avaliação da compra": 5,
            "Tipo de pagamento": "Cartão de crédito",
            "Quantidade de parcelas": 2,
            "Latitude": -8.0476,
            "Longitude": -34.8770
        },
        {
            "Produto": "Teclado Mecânico",
            "Categoria do Produto": "Eletrônicos",
            "Preço": 199.99,
            "Frete": 12.00,
            "Data da Compra": "20/06/2023",
            "Vendedor": "Kabum",
            "Local da compra": "Online",
            "Avaliação da compra": 4,
            "Tipo de pagamento": "Boleto",
            "Quantidade de parcelas": 1,
            "Latitude": -23.5505,
            "Longitude": -46.6333
        }
    ]
    print("🔹 Inserting test documents...")
    insert_data(collection, data)
    
    # 3. Visualize all documents
    print("\n📂 Documents in the collection:")
    # visualize_collection(collection)
    
    # 4. Rename a column ('Preço' to 'preco')
    rename_columns(collection, "Preço", "preco")
    
    # 5. Filter by category
    books = select_category(collection, "Livros")
    print("\n📘 Products in category 'Livros':")
    # for book in books:
    #     print(book)
        
    # 6. Filter by date using regex (e.g., purchases in 2023)
    products_2023 = make_regex(collection, "2023")
    print("\n📅 Products with purchase dates in 2023:")
    # for product in products_2023:
    #     print(product)
     
    # 7. Create DataFrame from books
    df = create_dataframe(books)
    df = rename_df_columns(df)
    df = format_date(df)
    
    print("\n📊 Final DataFrame:")
    print(df.head())
    
    # 8. Save to CSV
    save_csv(df, "data/products_test.csv")
    
    print("\n✅ Test pipeline completed.")
    
    
   
 
    