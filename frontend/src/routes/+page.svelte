
<script>
  import { onMount } from 'svelte';
  import * as echarts from 'echarts';

  let chartElement;

  const stats = [
    { title: 'Выручка', value: '₽ 248 500', change: '+12.8%', icon: '₽' },
    { title: 'Клиенты', value: '1 284', change: '+8.2%', icon: '👥' },
    { title: 'Сделки', value: '186', change: '+5.4%', icon: '📊' },
    { title: 'Конверсия', value: '24.8%', change: '+2.1%', icon: '↗' }
  ];

  const clients = [
    { name: 'Александр Иванов', company: 'ООО Альфа', amount: '₽ 45 000', status: 'Активен' },
    { name: 'Мария Петрова', company: 'ООО Вектор', amount: '₽ 32 500', status: 'Новый' },
    { name: 'Дмитрий Смирнов', company: 'ООО Техно', amount: '₽ 78 000', status: 'Активен' },
    { name: 'Елена Козлова', company: 'ООО Прогресс', amount: '₽ 19 000', status: 'Ожидание' }
  ];

  onMount(() => {
    const chart = echarts.init(chartElement);

    chart.setOption({
      tooltip: { trigger: 'axis' },
      grid: { left: 45, right: 20, top: 30, bottom: 30 },
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
        axisLine: { show: false },
        axisTick: { show: false }
      },
      yAxis: {
        type: 'value',
        splitLine: { lineStyle: { color: '#eeeeee' } }
      },
      series: [{
        name: 'Выручка',
        type: 'line',
        smooth: true,
        data: [12000, 19000, 15000, 28000, 24000, 35000, 42000],
        symbolSize: 8,
        lineStyle: { width: 3, color: '#6366f1' },
        itemStyle: { color: '#6366f1' },
        areaStyle: { color: 'rgba(99, 102, 241, 0.10)' }
      }]
    });

    const observer = new ResizeObserver(() => chart.resize());
    observer.observe(chartElement);

    return () => {
      observer.disconnect();
      chart.dispose();
    };
  });
</script>

<svelte:head>
  <title>CRM — Аналитика</title>
  <meta name="description" content="Панель аналитики CRM" />
</svelte:head>

<div class="app">
  <aside class="sidebar">
    <div class="brand">◈ <span>DataCRM</span></div>

    <div class="nav-label">МЕНЮ</div>

    <nav>
      <a href="/" class="active">▦ <span>Дашборд</span></a>
      <a href="/clients">♙ <span>Клиенты</span></a>
      <a href="/deals">◇ <span>Сделки</span></a>
      <a href="/analytics">▤ <span>Аналитика</span></a>
    </nav>

    <div class="sidebar-bottom">
      <a href="/settings">⚙ <span>Настройки</span></a>
    </div>
  </aside>

  <main>
    <header>
      <div>
        <h1>Дашборд</h1>
        <p>Обзор показателей вашей CRM</p>
      </div>
      <div class="user">
        <div class="avatar">Д</div>
        <span>Администратор</span>
      </div>
    </header>

    <section class="stats">
      {#each stats as stat}
        <article class="card stat">
          <div class="stat-top">
            <span>{stat.title}</span>
            <span class="stat-icon">{stat.icon}</span>
          </div>
          <div class="stat-value">{stat.value}</div>
          <div class="change">{stat.change} <span>за месяц</span></div>
        </article>
      {/each}
    </section>

    <section class="card chart-card">
      <div class="section-heading">
        <div>
          <h2>Динамика выручки</h2>
          <p>Показатели за последние 7 дней</p>
        </div>
        <select aria-label="Период графика">
          <option>Последние 7 дней</option>
          <option>Последние 30 дней</option>
          <option>Последние 12 месяцев</option>
        </select>
      </div>
      <div class="chart" bind:this={chartElement}></div>
    </section>

    <section class="card table-card">
      <div class="section-heading">
        <div>
          <h2>Последние клиенты</h2>
          <p>Недавно добавленные записи</p>
        </div>
        <a href="/clients" class="all-link">Все клиенты →</a>
      </div>

      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Клиент</th>
              <th>Компания</th>
              <th>Сумма</th>
              <th>Статус</th>
            </tr>
          </thead>
          <tbody>
            {#each clients as client}
              <tr>
                <td>{client.name}</td>
                <td>{client.company}</td>
                <td>{client.amount}</td>
                <td>
                  <span class="status" class:waiting={client.status === 'Ожидание'} class:new={client.status === 'Новый'}>
                    {client.status}
                  </span>
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    </section>
  </main>
</div>

<style>
  :global(*) {
    box-sizing: border-box;
  }

  :global(body) {
    margin: 0;
    background: #f5f6fa;
    color: #202235;
    font-family: system-ui, sans-serif;
  }

  .app {
    min-height: 100vh;
    display: flex;
  }

  .sidebar {
    width: 235px;
    background: #202235;
    color: #fff;
    padding: 28px 18px;
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
  }

  .brand {
    font-size: 22px;
    font-weight: 750;
    margin: 0 0 48px 8px;
    color: #a5a6ff;
  }

  .brand span {
    color: white;
  }

  .nav-label {
    font-size: 11px;
    color: #888ba4;
    margin: 0 0 14px 10px;
    letter-spacing: 1px;
  }

  nav {
    display: grid;
    gap: 7px;
  }

  nav a, .sidebar-bottom a {
    display: flex;
    gap: 12px;
    padding: 12px;
    border-radius: 8px;
    color: #c4c5d2;
    text-decoration: none;
    font-size: 14px;
  }

  nav a.active {
    color: white;
    background: #4849a4;
  }

  nav a:hover, .sidebar-bottom a:hover {
    background: #34364e;
  }

  .sidebar-bottom {
    margin-top: auto;
  }

  main {
    flex: 1;
    min-width: 0;
    max-width: 1600px;
    padding: 36px;
    margin: 0 auto;
    width: 100%;
  }

  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
  }

  h1 {
    font-size: 27px;
    margin: 0 0 5px;
  }

  h2 {
    font-size: 17px;
    margin: 0 0 5px;
  }

  p {
    color: #85879a;
    font-size: 13px;
    margin: 0;
  }

  .user {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 13px;
  }

  .avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: grid;
    place-items: center;
    background: #e5e5ff;
    color: #5556bb;
    font-weight: 700;
  }

  .stats {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 18px;
    margin-bottom: 22px;
  }

  .card {
    background: white;
    border: 1px solid #ebecf1;
    border-radius: 12px;
    padding: 22px;
  }

  .stat-top {
    display: flex;
    justify-content: space-between;
    color: #77798b;
    font-size: 13px;
  }

  .stat-icon {
    font-size: 20px;
    color: #6969cf;
  }

  .stat-value {
    font-size: 27px;
    font-weight: 700;
    margin: 17px 0 9px;
  }

  .change {
    font-size: 12px;
    color: #15966a;
    font-weight: 650;
  }

  .change span {
    color: #999baa;
    font-weight: 400;
  }

  .chart-card, .table-card {
    margin-bottom: 22px;
  }

  .section-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
  }

  select {
    padding: 9px 12px;
    border: 1px solid #e5e6ec;
    border-radius: 7px;
    background: white;
    color: #555;
  }

  .chart {
    height: 300px;
    width: 100%;
    margin-top: 20px;
  }

  .all-link {
    color: #6263c5;
    text-decoration: none;
    font-size: 13px;
  }

  .table-wrapper {
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    text-align: left;
    font-size: 13px;
    white-space: nowrap;
  }

  th {
    color: #88899a;
    font-weight: 500;
    font-size: 12px;
  }

  th, td {
    padding: 15px 12px;
    border-bottom: 1px solid #f0f0f3;
  }

  td {
    color: #45475a;
  }

  .status {
    display: inline-block;
    padding: 5px 9px;
    border-radius: 20px;
    background: #e5f7ee;
    color: #16875c;
    font-size: 11px;
  }

  .status.new {
    background: #e9edff;
    color: #555cc0;
  }

  .status.waiting {
    background: #fff2df;
    color: #b7791f;
  }

  @media (max-width: 1000px) {
    .stats {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 650px) {
    .sidebar {
      width: 65px;
      padding: 20px 8px;
    }

    .brand {
      font-size: 20px;
      margin-left: 10px;
    }

    .brand span, .nav-label, nav a span, .sidebar-bottom span {
      display: none;
    }

    nav a, .sidebar-bottom a {
      justify-content: center;
      padding: 12px 5px;
    }

    main {
      padding: 20px 12px;
    }

    .user span {
      display: none;
    }

    .stats {
      gap: 10px;
    }

    .stat-value {
      font-size: 20px;
    }

    .card {
      padding: 15px;
    }

    .chart {
      height: 240px;
    }
  }
</style>
