const API_BASE = '/api';

export interface AutoApplyResponse {
  success: boolean;
  message: string;
  jobTitle?: string;
  company?: string;
  applicationId?: string;
}

export interface Preferences {
  keywords: string[];
  jobFilters: Record<string, any>;
  applicationSettings: Record<string, any>;
}

export const autoApply = async (preferences: Preferences): Promise<AutoApplyResponse> => {
  const response = await fetch(`${API_BASE}/auto-apply`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(preferences),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || 'Failed to apply');
  }

  return response.json();
};

