CREATE TABLE transacoes (
    id SERIAL PRIMARY KEY,
    id_transacao INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    cliente_id INT NOT NULL
);
