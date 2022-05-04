export default function guardrail(mathFunction) {
  const queue = [];
  const result = mathFunction();
  if (result instanceof Error) {
    queue.push(result.message);
    queue.push('Guardrail was processed');
  } else {
    queue.push(result);
    queue.push('Guardrail was processed');
  }
  return queue;
}
