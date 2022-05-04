export default function guardrail(mathFunction) {
  const queue = [];
  try {
    mathFunction();
  } catch (e) {
    queue.push(`${e.name}: ${e.message}`);
    queue.push('Guardrail was processed');
    return queue;
  }
  queue.push(mathFunction());
  queue.push('Guardrail was processed');
  return queue;
}
