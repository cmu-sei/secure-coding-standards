export default defineAppConfig({
  sitemap: {
    hostname: 'https://cmu-sei.github.io/secure-coding-standards/',
  },
  githubUrl: 'https://github.com/cmu-sei/secure-coding-standards',
  appSuitePrefix: 'SEI',
  appSuite: 'CERT',
  pageTitle: 'CERT Secure Coding',
  navigation: [
    { title: 'Home', path: '/' },
    {
      title: 'Coding Standards',
      path: '/coding-standards',
      children: [
        { title: 'Android Coding Standard', path: '/android-secure-coding-standard' },
        { title: 'C Coding Standard', path: '/sei-cert-c-coding-standard' },
        { title: 'C++ Coding Standard', path: '/sei-cert-cpp-coding-standard' },
        { title: 'Java Coding Standard', path: '/sei-cert-oracle-coding-standard-for-java' },
        { title: 'Perl Coding Standard', path: '/sei-cert-perl-coding-standard' },
      ]
    },
  ],
})
