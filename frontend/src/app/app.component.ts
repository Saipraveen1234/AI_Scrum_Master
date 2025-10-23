import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environment';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <main class="max-w-3xl mx-auto p-6">
      <h1 class="text-3xl font-bold mb-4">AI Scrum Master Dashboard</h1>

      <section class="p-4 bg-white shadow rounded">
        <h2 class="text-xl font-semibold mb-2">Database Connection</h2>
        <p *ngIf="status() === 'ok'" class="text-green-600">
          ✅ Backend Connected!
        </p>
        <p *ngIf="status() === 'fail'" class="text-red-600">
          ❌ Connection Failed
        </p>
      </section>
    </main>
  `,
})
export class AppComponent {
  status = signal<'ok' | 'fail' | 'checking'>('checking');

  constructor(private http: HttpClient) {
    this.checkBackend();
  }

  checkBackend() {
    this.http.get(`${environment.apiBaseUrl}/health`).subscribe({
      next: () => this.status.set('ok'),
      error: () => this.status.set('fail'),
    });
  }
}
