import { copyFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const targetDir = path.join(process.cwd(), 'tests', 'e2e');
const source = path.join(process.cwd(), 'db.json');
const target = path.join(targetDir, 'db.e2e.json');

await mkdir(targetDir, { recursive: true });
await copyFile(source, target);

console.log(`Đã reset database E2E: ${target}`);
