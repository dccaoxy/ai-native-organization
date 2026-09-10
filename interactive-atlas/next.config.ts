import type { NextConfig } from 'next';

const nextConfig: NextConfig = {
  // atlas.aegpc.cn serves the production build as static files through Nginx.
  // Emit direct image URLs instead of relying on the dynamic /_next/image route.
  images: {
    unoptimized: true,
  },
};

export default nextConfig;
