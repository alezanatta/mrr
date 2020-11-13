INSERT INTO dashboard_dimsegmento (nm_segmento) (SELECT DISTINCT a.segmento FROM stage.cliente a) ON CONFLICT DO NOTHING;
INSERT INTO dashboard_dimcliente (nr_cliente, nm_cliente) (SELECT DISTINCT a.id, a.nome FROM stage.cliente a) ON CONFLICT DO NOTHING;
INSERT INTO dashboard_dimlocalidade (nm_cidade, nm_estado) (SELECT DISTINCT a.cidade, a.estado FROM stage.cliente a) ON CONFLICT DO NOTHING;
INSERT INTO dashboard_dimplano (nm_plano) (SELECT DISTINCT a.tp_plano from stage.pagamento a) ON CONFLICT DO NOTHING;
