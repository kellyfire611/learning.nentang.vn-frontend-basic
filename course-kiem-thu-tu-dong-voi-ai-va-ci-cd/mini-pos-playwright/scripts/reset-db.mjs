import fs from 'node:fs';
import path from 'node:path';

const rootDir = process.cwd();
const seedPath = path.join(rootDir, 'db.seed.json');
const dbPath = path.join(rootDir, 'db.json');

fs.copyFileSync(seedPath, dbPath);

console.log('Đã reset db.json từ db.seed.json');
