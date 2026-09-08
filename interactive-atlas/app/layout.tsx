import type { Metadata } from 'next';
import { Geist, Geist_Mono } from 'next/font/google';
import './globals.css';

const geistSans = Geist({
  variable: '--font-geist-sans',
  subsets: ['latin'],
});

const geistMono = Geist_Mono({
  variable: '--font-geist-mono',
  subsets: ['latin'],
});

export const metadata: Metadata = {
  metadataBase: new URL('https://ai-native-organization-atlas.dccaoxy.chatgpt.site'),
  title: 'AI-Native Organization · Interactive Atlas',
  description: 'Explore the frozen Operating Model through World, Architecture, Knowledge, Authority, and Value views.',
  openGraph: {
    title: 'AI-Native Organization · Interactive Atlas',
    description: 'Explore one organizational reality through five connected views.',
    images: ['/og.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'AI-Native Organization · Interactive Atlas',
    description: 'Explore one organizational reality through five connected views.',
    images: ['/og.png'],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN" className="dark">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
