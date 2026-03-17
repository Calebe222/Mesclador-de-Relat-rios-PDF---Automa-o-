# 📄 Mesclador de Relatórios (PDF) - Automação 

Este script foi desenvolvido para automatizar a junção de relatórios mensais em PDF, garantindo que a ordem cronológica e numérica seja respeitada (ex: Relatório 1, 2, 10, 11...). 

Útil para organizar processos administrativos e consolidar documentos para sistemas como o SEI ou envios institucionais.

## 🚀 Funcionalidades
- **Ordenação Natural:** Utiliza a biblioteca `natsort` para que o arquivo "2" venha antes do "10" (diferente da ordenação padrão do computador).
- **Filtro Automático:** Ignora arquivos que não sejam PDF na pasta selecionada.
- **Segurança Offline:** O processamento é local, garantindo a privacidade dos dados públicos.

## 🛠️ Pré-requisitos
Antes de rodar o script, você precisa ter o Python instalado e as bibliotecas necessárias.

### 1. Instale as dependências
Abra o seu terminal e execute:
```bash
pip install -r requirements.txt