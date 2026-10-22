# Conclusões

[Início](../README.md) · [Anterior: evidências](07-evidencias.md) · [Próximo: referências](09-referencias.md)

O laboratório mostrou como credenciais padrão permitem acesso mesmo sem explorar uma falha de execução de código. Os testes com o Medusa foram simples, mas interpretar seus resultados exigiu conferir a aplicação, as permissões e os logs do servidor.

A investigação do SMB foi a parte que mais exigiu essa conferência. O módulo apresentou sucesso com uma referência a `ADMIN$`, enquanto a tentativa de listagem retornou acesso negado. Aumentar temporariamente o nível de log ajudou a confirmar que a senha estava correta. O resultado sustentava autenticação, mas não a conclusão de que havia acesso administrativo. O erro `BAD SIG` da consulta adicional permaneceu sem causa isolada.

No DVWA, comparar o código com os tempos ajudou a entender a diferença entre os níveis. O High acrescentou atraso após as falhas e aumentou o tempo do lote, mas a senha presente na lista continuou sendo aceita. Já os logs revelaram uma exposição independente da dificuldade selecionada: o formulário enviava a senha na URL, deixando os valores registrados no Apache.

Os retestes deram uma medida concreta do efeito das mudanças. Após trocar as senhas, as credenciais antigas deixaram de funcionar e as novas foram aceitas. Depois de restringir a enumeração anônima no Samba, a consulta usada anteriormente passou a falhar. Esses resultados confirmam o efeito das alterações sobre as condições testadas; a avaliação não mediu resistência a listas maiores ou a outras formas de acesso.

## O que eu melhoraria em uma próxima execução

Sincronizaria os relógios antes de começar e registraria os horários e o fuso junto de cada rodada. A divergência entre as VMs dificultou a leitura dos logs e exigiu comparar sequências e intervalos para correlacionar os eventos.

Também registraria a duração total nos três níveis do DVWA e faria repetições para comparar a variação. Isso permitiria uma análise de desempenho mais consistente do que usar apenas uma medição do High.

Como continuação técnica, avaliaria um controle de limitação de tentativas em um serviço suportado, definindo previamente o limite, a janela de observação e o procedimento de recuperação. A análise incluiria tanto a rejeição das tentativas automatizadas quanto a continuidade do acesso legítimo. Essa etapa é uma proposta futura.

A documentação reúne os resultados que consegui demonstrar e as dúvidas que permaneceram. Para mim, o aprendizado central foi acompanhar uma tentativa de ponta a ponta: o que foi enviado, como o serviço respondeu, o que ficou registrado e o que mudou depois da defesa.
