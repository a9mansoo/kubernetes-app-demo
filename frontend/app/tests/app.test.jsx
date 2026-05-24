import { render, screen } from '@testing-library/react';
import { vi, test, expect } from 'vitest';
import '@testing-library/jest-dom';
import App from '../src/App';

test('renders user after fetch', async () => {
  vi.stubGlobal(
    'fetch',
    vi.fn(() =>
      Promise.resolve({
        ok: true,
        json: () =>
          Promise.resolve({
            user: 'fakename',
          }),
      }),
    ),
  );

  render(<App />);

  expect(screen.getAllByText(/loading/i).length).toBeGreaterThan(0);

  expect(await screen.findByText('k8s cluster')).toBeInTheDocument();
  expect(await screen.getAllByText('fakename').length).toBeGreaterThan(0);
});
