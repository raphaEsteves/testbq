from controller.pioneer_badge_controller import (
	insert_item,
	list_all,
	select_by_id,
)

if __name__ == "__main__":

	dados = [
		{
					'pioneer_item_name': 'Resquício do Governante Selado (Vinculado)',
					'pioneer_item_cost': 72000,
					'pioneer_item_pre_requisits': 'P70 da Torre da Provação'
		},
		{
			'pioneer_item_name': 'Resquício do Imortal Selado (Vinculado)',
			'pioneer_item_cost': 72000,
			'pioneer_item_pre_requisits': 'P70 da Torre da Provação'
		},
		{
			'pioneer_item_name': 'Resquício do Transcendente Selado (Vinculado)',
			'pioneer_item_cost': 72000,
			'pioneer_item_pre_requisits': 'P70 da Torre da Provação'
		}
	]

# 	INSERT
# 	Função para inserir dados na tabela.
# 	insert_item(dados)

# 	SELECT
# 	print(list_all()) #Função que retorna o conteúdo da tabela

	# print(select_by_id('6784a50c-ebbd-4561-acc1-bdbe329000cd'))
