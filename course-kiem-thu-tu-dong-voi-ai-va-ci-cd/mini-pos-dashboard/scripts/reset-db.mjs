import { copyFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const rootDir = join(__dirname, '..');
const seedPath = join(rootDir, 'db.seed.json');
const dbPath = join(rootDir, 'db.json');

copyFileSync(seedPath, dbPath);
console.log('Đã reset db.json từ db.seed.json');
