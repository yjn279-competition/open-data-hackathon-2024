'use client'

import React from 'react';
import Charts from './Charts';
import UserList from './UserList';
import { dashboardData } from './server';

const Dashboard: React.FC = () => {
  return (
    <div className="container mx-auto p-4">
      <div className="bg-white shadow-lg rounded-lg p-6 mb-6">
        <Charts data={dashboardData} />
      </div>
      <div className="bg-white shadow-lg rounded-lg p-6">
        <UserList />
      </div>
    </div>
  );
};

export default Dashboard;
