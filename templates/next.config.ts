import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,

  output: 'standalone',

  compress: true,

  compiler: {
    removeConsole: true,
  },

};

export default nextConfig;
